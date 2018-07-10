from django.contrib import admin

from .models import UserProfile, Channel, ChannelType

class UserProfileChannelAdmin(admin.ModelAdmin):
     model= UserProfile
     filter_horizontal = ('fav_channels',) #If you don't specify this, you will get a multiple select widget.


admin.site.register(UserProfile, UserProfileChannelAdmin)
admin.site.register(Channel)
admin.site.register(ChannelType)