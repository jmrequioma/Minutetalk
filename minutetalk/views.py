from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import UserProfile, ChannelType, Channel
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class IndexView(generic.View):
    template_name = 'minutetalk/index.html'

    def get(self, request, *args, **kwargs):
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
        f = UserProfileForm()
        return render(request, 'minutetalk/index.html' ,{"form" : f})
        
    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data['username']
        password = data['password1']
        if(User.objects.filter(username=data).exists()):
            context = {"error": "Username is already taken"}
            return JsonResponse(context)
        else:
            user = User.objects.create_user(username=data["username"],password=data['password1'],email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
            userProfile = UserProfile(user=user,gender=data['gender'], age=data["age"])
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
        context = {
            'user': request.user,
            'channels_list' : channels_list,
        }
        return render(request, 'minutetalk/channel_view.html',context)

def sign_out(request):
    logout(request)
    return redirect('minutetalk:index')

def join_channel(request, channel):
    return render(request, 'minutetalk/channel.html', {'channel':channel})

def search_channel(request):
    username = request.GET.get('query')
    data = Channel.objects.filter(title__contains=username)
    context = [(x.title,x.description,x.img_src.name) for x in data]
    return JsonResponse({'titles' : context });