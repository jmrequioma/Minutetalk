from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "minutetalk"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LogInView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('home', views.HomeView.as_view(), name='home'),
    path('logout', views.sign_out, name='logout'),
    path('<str:channel>', views.join_channel, name='join_channel'),
    path('ajax/search/', views.search_channel, name='search_channel'),
    
]