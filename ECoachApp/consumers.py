from channels.generic.websocket import WebsocketConsumer
import json
class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({'lapNumber': 1, 'value': 5.4}))

'''
  var socket = new WebSocket('ws://localhost:8000/ws/')
  socket.onmessage = function(){
    var data = JSON.parse(event.data)
    console.log(data)
    document.querySelector('#value').innerText = data.value
  }

'''