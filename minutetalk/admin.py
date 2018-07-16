from django.contrib import admin

from .models import UserProfile, Channel, ChannelType, CallerCallee


class UserProfileChannelAdmin(admin.ModelAdmin):
    model = UserProfile
    # If you don't specify this, you will get a multiple select widget.
    filter_horizontal = ('fav_channels',)


admin.site.register(UserProfile, UserProfileChannelAdmin)
admin.site.register(Channel)
admin.site.register(ChannelType)
admin.site.register(CallerCallee)
