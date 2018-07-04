from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

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
            user = User.objects.create_user(email=data['email'], first_name=data['first_name'], username=data["username"],
            last_name=data['last_name'], password=data['password1'])
            userProfile = UserProfile(user=user,gender=data['gender'], age=data["age"])
            user = authenticate(request, username=username, password=password)
            if user is not None:
                userProfile.save()
                user.save()
                login(request, user)
                return JsonResponse({})
            return JsonResponse({"error": "Some error occured during sign up"})


def home(request):
    return render(request, 'minutetalk/channel_view.html')

def sign_out(request):
    logout(request)
    return redirect('minutetalk:index')

def join_channel(request, channel):
    return render(request, 'minutetalk/channel.html', {'channel':channel})

