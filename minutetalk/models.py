from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, default='example@email.com')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    img_src = models.FileField(upload_to='users/',default='users/noprof.jpg')
    channels = models.ManyToManyField('Channel')

    def __str__(self):
        return self.first_name

class ChannelType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Channel(models.Model):
    description = models.CharField(max_length=100, null=True)
    img_src = models.FileField(upload_to='channels/',default='channels/nopic.jpg')
    title = models.CharField(max_length=20, null=True)
    channel_type = models.ForeignKey('ChannelType', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ChannelUser(models.Model):
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)