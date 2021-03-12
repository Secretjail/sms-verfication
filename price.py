import os
from time import sleep

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from pprint import pprint

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)
price = {'ADAUSDT': None, 'error':False}

def btc_pairs_trade(msg):
	''' define how to process incoming WebSocket messages '''
	print(msg)
	if msg['e'] != 'error':
		price['ADAUSDT'] = float(msg['c'])
	else:
		price['error']:True

while not price['ADAUSDT']:
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
		print(price['ADAUSDT'])
		if price['ADAUSDT'] > 1.1300 :
			try:
				print('order = client.order_market_buy')
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
