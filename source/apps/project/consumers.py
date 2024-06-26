from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('notifications_group', self.channel_name)
        print('connect...')
        await self.accept()

    async def disconnect(self, close_code):
        print('disconnect...')
        await self.channel_layer.group_discard('notifications_group', self.channel_name)

    async def send_notification(self, event):
        print(event)
        await self.send(text_data=json.dumps(event['message']))