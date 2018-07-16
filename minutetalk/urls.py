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
    path('<int:channel_id>', views.JoinChannel.as_view(), name='join_channel'),
    path('edit_profile', views.EditProfile.as_view(), name='edit_profile'),
    path('videochat', views.VideoChatView.as_view(), name='favorite'),

    path('ajax/search', views.SearchChannel.as_view(), name='search_channel'),
    path('ajax/add_to_favorite', views.AddFavoriteChannel.as_view(), name='favorite'),
    path('ajax/session', views.CreateSessionView.as_view(), name='create_session'),
]