from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

class IndexView(generic.View):
    template_name = 'minutetalk/index.html'

    def get(self, request, *args, **kwargs):
        f = UserProfileForm()
        return render(request, self.template_name)

class LogInView(generic.View):
    template_name = 'minutetalk/index.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({})
        context = {
            "error": "Username or Password is incorrect"
        }
        return JsonResponse(context)

class SignUpView(generic.View):
    model = User
    
    def get(self, request, *args, **kwargs):
        f = UserProfileForm()
        return render(request, 'minutetalk/index.html' ,{"form" : f})
        
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password1']
        f = UserProfileForm(request.POST)
        if f.is_valid():
            print('Success')
            f.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({})
        print(f.errors)
        context = {
            "error": "Username is already taken"
        }
        return JsonResponse(context)

def home(request):
    return render(request, 'minutetalk/home.html')
