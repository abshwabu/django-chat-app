import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(
            text_data=json.dumps({
                'type':'connection_established',
                'message':'you are connected'
            })
        )
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print('message: %s' % message)

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
        