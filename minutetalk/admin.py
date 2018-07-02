from django.contrib import admin

from .models import UserProfile, Channel

admin.site.register(UserProfile)
admin.site.register(Channel)