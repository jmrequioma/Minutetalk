from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    img_src = models.ImageField(upload_to='users/', default='users/noprof.jpg')
    fav_channels = models.ManyToManyField('Channel', null=True, blank=True)
    my_channel = models.ForeignKey('Channel', on_delete=models
                                   .CASCADE, blank=True, null=True,
                                   related_name="current_channel")
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def asdict(self):
        return {
                'username': self.user.username,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'id': self.id,
                'img_src': self.img_src.name,
                'age': self.age,
                'gender': self.gender
                }

class ChannelType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Channel(models.Model):
    description = models.CharField(max_length=900, null=True)
    img_src = models.FileField(
        upload_to='channels/', default='channels/nopic.jpg')
    channel_type = models.ForeignKey('ChannelType', on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=20, null=True)
    url = models.CharField(max_length=40, null=True, blank=True)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Channel: {} , id : {}'.format(self.title,str(self.id))

class ChatLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    token = models.CharField(max_length=400,blank=True)
    session_id = models.CharField(max_length=72,blank=True)
    channel =models.ForeignKey('Channel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'User : {} \n Session : {} \n Token : {}'.format(self.user.username,
                                                    self.session_id, self.token)

class Question(models.Model):
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return 'Channel : {} \n Question : {} id : {}'.format(self.channel.title,
                                                    self.text,str(self.id))

class Payment(models.Model):
    email = models.EmailField()
    cardname = models.CharField(max_length=20)
    cardnumber = models.CharField(max_length=16)
    expirydate = models.CharField(max_length=10)
    cvc = models.CharField(max_length=4)

