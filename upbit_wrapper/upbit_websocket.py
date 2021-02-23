from websocket import WebSocketApp
from threading import Thread
import json
import time
class UpbitWebSocket:
    def __init__(self, request, callback=print):
        self.request = request
        self.callback = callback
        self.ws = WebSocketApp(
            url="wss://api.upbit.com/websocket/v1",
            on_message=lambda ws, msg: self.on_message(ws, msg),
            on_error=lambda ws, msg: self.on_error(ws, msg),
            on_close=lambda ws:     self.on_close(ws),
            on_open=lambda ws:     self.on_open(ws))
        self.running = False
    
    def on_message(self, ws, msg):
        msg = json.loads(msg.decode('utf-8'))
        self.callback(msg)
    
    def on_error(self, ws, msg):
        self.callback(msg)
    
    def on_close(self, ws):
        self.callback("closed")
        self.running = False

    def on_open(self, ws):
        th = Thread(target=self.activate, daemon=True)
        th.start()
    
    def activate(self):
        self.ws.send(self.request)
        while self.running:
            time.sleep(1)
        self.ws.close()
    
    def start(self):
        self.running = True
        self.ws.run_forever()

def aa(bb):
    print(bb)

if __name__ == "__main__":
    request='[{"ticket":"KRT-BTC"},{"type":"ticker","codes":["KRW-BTC"]}]'
    real = UpbitWebSocket(request=request,callback=aa)
    real.start()