from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
class IndexView(generic.View):
    template_name = 'minutetalk/index.html'

    def get(self, request, *args, **kwargs):
        f = UserProfileForm()
        return render(request, self.template_name)

class LogInView(generic.View):
    model = User
    template_name = 'minutetalk/index.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('minutetalk:home')
        context = {
        	"login_error" : "Incorrect username or password"
        }
        print("fail")
        return render(request, self.template_name, context)

class SignUpView(generic.View):
    model = User
    template_name = 'minutetalk/index.html'

    def get(self, request, *args, **kwargs):
        f = UserProfileForm()
        return render(request, self.template_name,{"form" : f})
        
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
                return redirect('minutetalk:home')
        else:
            return render(request,'minutetalk/index.html',{'signup_error': 'Username is already taken'})

def home(request):
    return render(request, 'minutetalk/home.html')
