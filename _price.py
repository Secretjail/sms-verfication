import asyncio
import websockets
import os
from time import sleep

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)
price = {'BTCUSDT': None, 'error':False}

async def candle_stick_data():
    url = "wss://stream.binance.com:9443/ws/" #steam address

    

    first_pair = 'bnbbtc@kline_1m' #first pair
    async with websockets.connect(url+first_pair) as sock:
        pairs = '{"method": "SUBSCRIBE", "params": ["xrpbtc@kline_1m","ethbtc@kline_1m" ],  "id": 1}' #other pairs
        await sock.send(pairs)
        print(f"> {pairs}")
        while True:
            resp = await sock.recv()
            print(f"< {resp}")

asyncio.get_event_loop().run_until_complete(candle_stick_data())

'''

def btc_pairs_trade(msg):
	if msg['e'] != 'error':
		price['BTCUSDT'] = float(msg['c'])
	else:
		price['error']:True

while not price['BTCUSDT']:
	# wait for WebSocket to start streaming data
	sleep(0.1)
while True:
	# error check to make sure WebSocket is working
	if price['error']:
		# stop and restart socket
		bsm.stop_socket(conn_key)
		bsm.start()
		price['error'] = False

	else:
		if price['BTCUSDT'] > 10000:
			try:
				order = client.order_market_buy(symbol='ETHUSDT', quantity=100)
				break
			except BinanceAPIException as e:
				# error handling goes here
				print(e)
			except BinanceOrderException as e:
				# error handling goes here
				print(e)
	sleep(0.1)

bsm.stop_socket(conn_key)
reactor.stop()
'''
