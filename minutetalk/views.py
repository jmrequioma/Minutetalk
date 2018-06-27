from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
class IndexView(generic.View):
    template_name = 'minutetalk/index.html'

    def get(self, request, *args, **kwargs):
        f = UserProfileForm()
        return render(request, self.template_name,{"form" : f})

class LogInView(generic.View):
    model = User
    template_name = 'minutetalk/index.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        context = {
        	"error_message" : "Incorrect username or password"
        }
        return render(request, self.template_name,context)

class SignUpView(generic.View):
    model = User
    template_name = 'minutetalk/index.html'

    def get(self, request, *args, **kwargs):
        f = UserProfileForm()
        return render(request, self.template_name,{"form" : f})
        
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        f = UserCreationForm(request.POST)
        if f.is_valid():
            print('Success')
            form = UserProfileForm(request.POST)
            form.save()
            if user is not None:
                login(request, user)
                # return HttpResponseRedirect(reverse('minutetalk:home'))
                return render(request,'minutetalk/home.html')

        else:
            errors = f.errors
            form = UserProfileForm(request.POST)
            print('Fail')
            return render(request,'minutetalk/index.html',{'form':form, "errors" : f})