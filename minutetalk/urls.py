from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "minutetalk"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LogInView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('r1',views.r1, name='r1'),
    path('r2',views.r2, name='r2'),
    path('home', views.home, name='home')
    # path('/logout', views.index, name='logout'),
]