from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    img_src = models.FileField(upload_to='users/',default='users/noprof.jpg')
    fav_channels = models.ManyToManyField('Channel', null=True)
    my_channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True, related_name="current_channel")

    def __str__(self):
        return self.user.first_name

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