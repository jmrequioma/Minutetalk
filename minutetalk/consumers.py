import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Channel, ChatLog
from django.shortcuts import get_object_or_404


class ChatConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print('ChatConsumer', event)
        user = self.scope['user']
        self.channel_id = self.scope['path'][1:]
        user.userprofile.my_channel = get_object_or_404(Channel, id=self.channel_id)
        user.userprofile.save()
        
        await(self.channel_layer.group_add)(
            self.channel_id,
            self.channel_name
        )

        user_dict = {
            'type' : 'user',
            'join' : True,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'id': user.userprofile.id,
            'img_src': user.userprofile.img_src.name
        }

        await self.channel_layer.group_send(
            self.channel_id,
            {
                "type": "channel.join",
                "user": json.dumps(user_dict),
            }

        )

        await self.send({
            "type" : "websocket.accept",
        })

    async def channel_join(self, event):
       
        await self.send({
            "type": "websocket.send",
            "text": event['user'],
            })

    async def websocket_disconnect(self, event):

        # clear the data in database
        user = self.scope['user']
        user.userprofile.my_channel = None
        user.userprofile.save()
        user_dict ={
            'type' : 'user',
            'join' : False,
            'username': user.username,
            'id': user.userprofile.id,
        }
        await self.channel_layer.group_send(
            self.channel_id,
            {
                "type": "channel.quit",
                "user": json.dumps(user_dict)
            }

        )

        await self.channel_layer.group_discard(
            self.channel_id, 
            self.channel_name
        )
        print("disconnect", event)

    async def channel_quit(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['user']
            })
    
    async def websocket_receive(self, event):
        data = json.loads(event['text'])
        data['user'] = self.scope['user'].userprofile.asdict()
        await self.channel_layer.group_send(
            self.channel_id,
            {
                "type": "talk",
                "data": json.dumps(data)
            }
        )

    async def talk(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['data']
            })


class MessageConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        # print('MessageConsumer', event)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        chatLog = get_object_or_404(ChatLog, user=self.scope['user'])
        chatLog.delete()
        print("disconnnnnnnnnnnnnnnnnnnnnnnnnnnnect")

        # ChatLog.objects.filter(user=request.user).delete()
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'data': text_data_json,
            }
        )
     

    # Receive message from room group
    async def chat_message(self,event):
        message = event['data']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

  