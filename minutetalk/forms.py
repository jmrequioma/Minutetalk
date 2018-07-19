from django import forms
from .models import UserProfile, Channel, ChannelType, Payment
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import  get_object_or_404


class UserProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    age = forms.IntegerField()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['age', 'email', 'gender', 'username',
                  'password1', 'password2', 'first_name', 'last_name']

    def edit(self, request):
        data = self.cleaned_data
        user = request.user
        userProfile = request.user.userprofile

        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        userProfile.age = data['age']
        userProfile.gender = data['gender']
        user.save()
        userProfile.save()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken')
        return username

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('User must be 18 years old or above')
        return age

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Password does not match')
        return password1


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ChannelForm(forms.ModelForm):

    channel_type = forms.ModelChoiceField(queryset=ChannelType.objects.all(), to_field_name="name")
    title = forms.CharField()
    description = forms.CharField()
    url = forms.URLField()

    class Meta:
        model = Channel
        fields = ['channel_type', 'description', 'url', 'title']



    def clean_channel_type(self):
        channel_type = self.cleaned_data['channel_type']
        if not ChannelType.objects.filter(name=channel_type).exists():
            raise forms.ValidationError('Channel Type {} does not exists.'.format(channel_type))
        return channel_type

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'channel_type' in self.cleaned_data:
            channel_type = self.cleaned_data['channel_type']
            channels = get_object_or_404(ChannelType, name__iexact=channel_type).channel_set.all()
            if channels.filter(title__iexact=title).exists():
                raise forms.ValidationError('{} already exists in {} Channel Type.'.format(title, channel_type))
            return title
        else:
            raise forms.ValidationError('Channel Type cannot be empty')


    def clean_description(self):
        desc = self.cleaned_data['description']
        if len(desc) > 100:
            raise forms.ValidationError('Description must not exceed 100 characters')
        return desc



class PaymentForm(forms.ModelForm):
    email = forms.EmailField()
    cardname = forms.CharField()
    cardnumber = forms.CharField(max_length=16)
    expirydate = forms.CharField()
    cvc = forms.CharField(max_length=4)
    
    class Meta:
        model = Payment
        fields = ['email', 'cardname', 'cardnumber', 'expirydate', 'cvc']


