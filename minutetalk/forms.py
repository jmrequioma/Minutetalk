from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    age = forms.IntegerField()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    img_src = forms.CharField()
 
    class Meta:
        model = UserProfile
        fields = ['age','email','gender','username','password1','password2','first_name','last_name','img_src']

    def save(self, commit=True):
        data = self.cleaned_data
        user = User.objects.create_user(username=data["username"],password=data['password1'],email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        userProfile = UserProfile(user=user,gender=data['gender'], age=data["age"], img_src=data['img_src'])
        userProfile.save()

    def edit(self,request):
        data = self.cleaned_data
        user = request.user
        userProfile = request.user.userprofile

        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        userProfile.age = data["age"]
        userProfile.gender = data["gender"]
        user.save()
        userProfile.save()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("User must be 18 years old or above")
        return age

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Password does not match")
        return password1