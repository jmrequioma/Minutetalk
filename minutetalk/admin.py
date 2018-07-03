from django.contrib import admin

from .models import UserProfile, Channel, ChannelType

admin.site.register(UserProfile)
admin.site.register(Channel)
admin.site.register(ChannelType)