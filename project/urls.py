from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('minutetalk/', include('minutetalk.urls')),
    path('admin/', admin.site.urls),
]