from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ("M" , "Male"),
        ("F" , "Female")
    )
    age = forms.IntegerField(label="How old are you")
    email = forms.EmailField(label = "Email Address")
    gender = forms.ChoiceField(label="Your gender preference", choices=GENDER_CHOICES)
    username = forms.CharField(label="Your Username")
    password1 = forms.CharField(label="Your Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Your Password", widget=forms.PasswordInput)
    first_name = forms.CharField(label = "Name")
    last_name = forms.CharField(label = "Surname")
 
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "email", "username", "password1", "password2", "age","gender")

    def save(self, commit=True):
        data = self.cleaned_data
        user = User(email=data['email'], first_name=data['first_name'], username=data["username"],
        last_name=data['last_name'], password=data['password1'])
        user.save()
        userProfile = UserProfile(user=user,gender=data['gender'], age=data["age"])
        userProfile.save()