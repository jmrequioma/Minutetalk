import json
from channels.consumer import AsyncConsumer



class ChatConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("connected", event)
        user = self.scope['user']
        self.channel_id = self.scope['path'][1:]

        await(self.channel_layer.group_add)(
            self.channel_id,
            self.channel_name
        )

        user_dict ={
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
        print("recieve", event)
        data = json.loads(event['text'])
        data['type'] = 'talk'
        data['user'] = self.scope['user'].userprofile.asdict()
        await self.channel_layer.group_send(
            self.channel_id,
            {
                "type": "talk",
                "id": json.dumps(data)
            }
        )

    async def talk(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['id']
            })
