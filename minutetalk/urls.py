from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "minutetalk"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LogInView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('home', views.HomeView.as_view(), name='home'),
    path('logout', views.SignOut.as_view(), name='logout'),
    path('edit_profile', views.EditProfile.as_view(), name='edit_profile'),
    path('edit_pass', views.EditPassword.as_view(), name='edit_password'),
    path('<int:channel_id>', views.JoinChannel.as_view(), name='join_channel'),
    path('<int:channel_id>/videochat', views.VideoChatView.as_view(), name='videochat'),
    path('advertise', views.AdvertiseView.as_view(), name='advertise'),

    path('ajax/delete_session', views.DeleteSession.as_view(), name='delete_session'),
    path('ajax/advertise', views.ValidateAdvertise.as_view(), name='validate_advertise'),
    path('ajax/token', views.CreateToken.as_view(), name='token'),
    path('ajax/search_channel', views.SearchChannel.as_view(), name='search_channel'),
    path('ajax/search_user', views.SearchUser.as_view(), name='search_user'),
    path('ajax/check_password', views.CheckPassword.as_view(), name='check_password'),
    path('ajax/add_to_favorite', views.AddFavoriteChannel.as_view(), name='favorite'),
    path('ajax/session', views.CreateSession.as_view(), name='create_session'),
]