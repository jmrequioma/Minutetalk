from django.contrib import admin

from .models import UserProfile, Channel, ChannelType, ChannelUser

admin.site.register(UserProfile)
admin.site.register(Channel)
admin.site.register(ChannelType)
admin.site.register(ChannelUser)