from django.conf.urls import url
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('<int:id>', consumers.ChatConsumer),
    path('videochat/<slug:room_name>', consumers.MessageConsumer),
    # url(r'^(?P<room_name>[^/]+)/videochat$', consumers.MessageConsumer),
]