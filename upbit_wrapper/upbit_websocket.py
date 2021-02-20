# https://docs.upbit.com/docs/upbit-quotation-websocket

import json
import time
import logging
from websocket import WebSocketApp
from threading import Thread

class UpbitWebSocket:
    def __init__(self, request):
        self.request = request
        self.logger = logging.getLogger("UpbitWebSocket")
        self.ws = WebSocketApp(
            url="wss://api.upbit.com/websocket/v1",
            on_message=lambda ws, msg: self.on_message(ws, msg),
            on_error=lambda ws, msg: self.on_error(ws, msg),
            on_close=lambda ws:     self.on_close(ws),
            on_open=lambda ws:     self.on_open(ws))
        self.running = False
    
    def on_message(self, ws, msg):
        msg = json.loads(msg.decode('utf-8'))
        self.logger.debug(msg)
    
    def on_error(self, ws, msg):
        self.logger.error(msg)
    
    def on_close(self, ws):
        self.logger.info("closed")
        self.running = False
    
    def on_open(self, ws):
        th = Thread(target=self.activate, daemon=True)
        th.start()
    
    def activate(self):
        self.ws.send(self.request)
        while self.running:
            time.sleep(5)
        self.ws.close()
    
    def start(self):
        self.running = True
        self.ws.run_forever()
