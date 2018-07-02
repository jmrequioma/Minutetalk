from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    img_src = models.FileField(upload_to='users/',default='users/noprof.jpg')

    def __str__(self):
        return self.user.username

class Channel(models.Model):
    description = models.CharField(max_length=100, null=True)
    img_src = models.FileField(upload_to='channels/',default='channels/nopic.jpg')
    title = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title