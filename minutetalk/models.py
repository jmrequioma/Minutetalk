from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    img_src = models.FileField(upload_to='users/',default='users/noprof.jpg')

    def __str__(self):
        return self.user.username