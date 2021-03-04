#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, pprint
#import syssys
#import requests
import json
from binance.enums import *

from binance.client import Client

from binance.websockets import BinanceSocketManager


# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)

bm = BinanceSocketManager(client)



def process_message(msg):
    print(msg)
    #print("message type: {}".format(msg['e']))
    #json_message=json.dumps(msg)
    #print('msg')
    #pprint.pprint(json_message)
    #candle=msg['p']
    #print(candle)



# do somethingdef process_message(msg):
    #print("message type: {}".format(msg['e']))
    #print(candle)
    # do something
# start any sockets here, i.e a trade socket
#conn_key = bm.start_trade_socket('ADAUSDT', process_message)

#kline
conn_key = bm.start_kline_socket('BNBBTC', process_message, interval=KLINE_INTERVAL_3MINUTE)

# then start the socket manager
bm.start()
