import os,sys

from binance.enums import *
from binance.client import Client
from binance.websockets import BinanceSocketManager
from pprint import pprint

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)

bm = BinanceSocketManager(client)
c=1
def process_message(msg):
    global c
    #pprint(msg['k']['c'])
    #print("=================")
    price=float(msg['p'])
    if price < float(sys.argv[1]):
        print(str(c) + '-buy buy buy')
        pprint(msg)
    else :
       print(str(c) + '-wait wait wait')
    c+=1

# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('ADAUSDT', process_message)

#kline
#conn_key = bm.start_kline_socket('ADAUSDT', process_message, interval=KLINE_INTERVAL_3MINUTE)

# then start the socket manager
bm.start()
