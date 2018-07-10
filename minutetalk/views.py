from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import UserProfile, ChannelType, Channel
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json

class IndexView(generic.View):
    template_name = 'minutetalk/index.html'

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return HttpResponseRedirect(reverse('minutetalk:home'))
        return render(request, self.template_name)

class LogInView(generic.View):
    template_name = 'minutetalk/index.html'

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
    def get(self, request, *args, **kwargs):
        return render(request, 'minutetalk/index.html' ,{"form" : f})
        
    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data['username']
        password = data['password1']
        if(User.objects.filter(username=username).exists()):
            context = {"error": "Username is already taken"}
            return JsonResponse(context)
        else:
            user = User.objects.create_user(username=data["username"],password=data['password1'],email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
            userProfile = UserProfile(user=user,gender=data['gender'], age=data["age"], email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
            user = authenticate(request, username=username, password=password)
            if user is not None:
                userProfile.save()
                user.save()
                login(request, user)
                return JsonResponse({})
            return JsonResponse({"error": "Some error occured during sign up"})

class HomeView(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        channels_list = ChannelType.objects.all()
        my_channels = UserProfile.objects.get(id=request.user.userprofile.id).fav_channels.all()
        context = {
            'user': request.user,
            'channels_list' : channels_list,
            'my_channels' : my_channels,
        }
        return render(request, 'minutetalk/channel_view.html',context)

def sign_out(request):
    logout(request)
    return redirect('minutetalk:index')

def join_channel(request, channel_id):
    channel = get_object_or_404(Channel,id=channel_id)
    user = UserProfile.objects.get(user=request.user)
    my_channels = user.fav_channels.all()
    user.my_channel = channel
    user.save()
    online_users = channel.current_channel.exclude(user=request.user)
    print(online_users)
    context = {
            'channel' : channel,
            'my_channels' : my_channels,
            'users': online_users,
            'fav' : user.fav_channels.filter(id=channel_id).exists()
        }
    return render(request, 'minutetalk/channel.html',context)

def search_channel(request):
    username = request.GET.get('query')
    data = Channel.objects.filter(title__contains=username)
    context = []
    for x in data:
        d = {
            'title' : x.title,
            'description' : x.description,
            'src' : x.img_src.name,
            'id' : x.id        
        }
        context.append(d)
    # context = [(x.title,x.description,x.img_src.name,x.id) for x in data]
    return JsonResponse({'titles' : context })

def edit_profile(request):
    data = request.POST
    user = request.user
    userProfile = request.user.userprofile
    user.first_name = userProfile.first_name = data["first_name"]
    user.last_name = userProfile.last_name = data["last_name"]
    user.email = userProfile.email = data["email"]
    userProfile.age = data["age"]
    userProfile.gender = data["gender"]
    if data["password1"]:
        user.set_password(data['password1'])

    user.save()
    userProfile.save()
    print(user.first_name)
    return JsonResponse({})

def addFavoriteChannel(request):
    channel_id = request.GET.get('channel_id');
    user = UserProfile.objects.get(user=request.user)
    print(user)
    channel = Channel.objects.get(id=request.GET.get('channel_id'))
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
