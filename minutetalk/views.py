from .models import UserProfile, ChannelType, Channel, ChatLog
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import UserProfileForm
from django.views import generic
from django.urls import reverse
from opentok import OpenTok
import base64

api_key = '46151822'
api_secret = '224a06a7055d1c1f5518d6a0de1720e71fb11e3c'
opentok = OpenTok(api_key, api_secret)


class IndexView(generic.View):

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return HttpResponseRedirect(reverse('minutetalk:home'))
        return render(request, 'minutetalk/index.html')


class LogInView(generic.View):

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({})
        context = {
            "error": "Username or Password is incorrect"
        }
        return JsonResponse(context)


class SignUpView(generic.View): 

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            data = request.POST
            print('DATA: ')
            print(data)
            user = User.objects.create_user(
                username=data['username'], password=data['password1'], 
                email=data['email'], first_name=data['first_name'], 
                last_name=data['last_name']
            )
            userprofile = UserProfile(
                user=user, gender=data['gender'], age=data['age']
            )
            userprofile.save()
            print(data['img_src'])
            if data['img_src']:
                addUserImage(request, userprofile)

            user = authenticate(
                request, username=request.POST['username'], 
                password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return JsonResponse({})
            return JsonResponse({"error": "Some error occured during sign up"})
        return JsonResponse({"error": form.errors})


class HomeView(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        channels_list = ChannelType.objects.all()
        my_channels = get_object_or_404(
            UserProfile, user=request.user).fav_channels.all()
        context = {
            'user': request.user,
            'channels_list': channels_list,
            'my_channels': my_channels,
        }
        return render(request, 'minutetalk/channel_view.html', context)


class SignOut(generic.View):

    def get(self, request):
        logout(request)
        return redirect('minutetalk:index')


class JoinChannel(LoginRequiredMixin, generic.View):

    def get(self, request, channel_id):
        channel = get_object_or_404(Channel, id=channel_id)
        user = request.user.userprofile
        online_users = channel.current_channel.exclude(user=request.user)
        my_channels = user.fav_channels.all()
        user.my_channel = channel
        user.save()
        context = {
            'channel': channel,
            'my_channels': my_channels,
            'users': online_users,
            'fav': user.fav_channels.filter(id=channel_id).exists()
        }
        return render(request, 'minutetalk/channel.html', context)


class SearchChannel(LoginRequiredMixin, generic.View):

    def get(self, request):
        username = request.GET.get('query')
        data = Channel.objects.filter(title__contains=username)
        context = []
        for x in data:
            d = {
                'title': x.title,
                'description': x.description,
                'src': x.img_src.name,
                'id': x.id
            }
            context.append(d)
        return JsonResponse({'titles': context})


class EditProfile(LoginRequiredMixin, generic.View):

    def post(self, request):
        # form = UserProfileForm(request.POST)
        # if form.is_valid():
            # form.edit(request)
            # print(request.POST['password1'])
        data = request.POST
        if (request.user.check_password(request.POST['password1'])): 
            user = request.user
            userProfile = request.user.userprofile
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            userProfile.age = data["age"]
            userProfile.gender = data["gender"]
            user.save()
            userProfile.save()
            return JsonResponse({})

        else:    
            return JsonResponse({'error': 'Password is incorrect'})


class EditPassword(LoginRequiredMixin, generic.View):

    def post(self, request):
        # form = UserProfileForm(request.POST)
        # if form.is_valid():
            # form.edit(request)
            # print(request.POST['password1'])
        data = request.POST
        user = request.user
        if (not user.check_password(request.POST['oldpassword'])): 
            return JsonResponse({'error': 'Current Password is incorrect'})
        if(data['password1'] != data['password2']):
            return JsonResponse({'error': 'New Password and Confirm Password do not match'})

        user.set_password(data['password1'])
        user.save()
        return JsonResponse({})

class CheckPassword(LoginRequiredMixin, generic.View):

    def get(self, request):
        
        if (request.user.check_password(request.GET['password'])): 
            return JsonResponse({'password_match': True})
        else:
           return JsonResponse({'password_match':False})


class AddFavoriteChannel(LoginRequiredMixin, generic.View):

    def get(self, request):
        channel_id = request.GET.get('channel_id')
        user = get_object_or_404(UserProfile, user=request.user)
        channel = get_object_or_404(Channel, id=request.GET.get('channel_id'))
        context = {}
        if user.fav_channels.filter(id=channel_id).exists():
            print('Removing from favorite channels...')
            context['message'] = 'Removed from favorites'
            user.fav_channels.remove(channel)
            return JsonResponse(context)
        else:
            print('Adding to favorite channels...')
            print(user.fav_channels.all())
            print(channel)
            user.fav_channels.add(channel)
            user.save()
            context['message'] = 'Added to favorites'
            return JsonResponse(context)


class VideoChatView(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        chatlog = ChatLog.objects.filter(user=request.user).last()
        
        context = {
            'apikey' : api_key,
            'session_id' : chatlog.session_id,
            'token' : chatlog.token,
            'message' : 'Enjoy'
        }
        return render(request, 'minutetalk/livestream.html',context)


class CreateToken(LoginRequiredMixin, generic.View):
    
    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        # Generate a Token from just a session_id (fetched from a database)
        token = opentok.generate_token(session_id
)
        connectionMetadata = request.user.username
        token = opentok.generate_token(session_id)

        chatlog = ChatLog(user=request.user,token=token,session_id=session_id)
        chatlog.save()

        context = {
            'apikey' : api_key,
            'session_id' : session_id,
            'token' : token,
            'message' : 'Chatlog created'
        }
        return JsonResponse(context)

class CreateSession(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        # Create a session that attempts to send streams directly between 
        # clients (falling back
        # to use the OpenTok TURN server to relay streams if the clients 
        # cannot connect):
        session = opentok.create_session()

        # Store this session ID in the database
        session_id = session.session_id
        # caller = request.user
        # callee = get_object_or_404(User, id=request.GET['callee_id'])

        # chatSession = CallerCallee(
        #     caller=caller, callee=callee, session_id=session_id
        # )
        # chatSession.save()
        context = {
            'message' : 'Video Session created successfully',
            'session' : session_id,  
        }
        return JsonResponse(context)

# Converts base64 image to Contentfile


def addUserImage(request, userprofile):
    image_data = request.POST['img_src']
    format, imgstr = image_data.split(';base64,')
    print("format", format)
    ext = format.split('/')[-1]

    data = ContentFile(base64.b64decode(imgstr))
    file_name = userprofile.user.username + ext
    userprofile.img_src.save(file_name, data, save=True)
