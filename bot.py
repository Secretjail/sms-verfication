
import os, pprint
#import syssys
#import requests
import json

from binance.client import Client

from binance.websockets import BinanceSocketManager

import websocket

SOCKET="wss://stream.binance.com:9443/ws/ethusdt@kline1m>"

def on_open(ws):
	print('opend conn')

def on_close(ws):
	print('closed conn')

def on_message(ws,message):
	print('recived message')

ws=websocket.WebSocketApp(SOCKET, on_open=on_open, onclose=on_close, on_messge=on_message)
ws.run_forever()
