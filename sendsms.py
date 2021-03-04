#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
import requests
import json

from binance.client import Client
from kavenegar import *

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)

# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol="BNBUSDT")

# print full output (dictionary)

symbol = btc_price['symbol']
price_not_rounded = btc_price['price']
price = price_not_rounded[:-6]

message = "قیمت {} \n {} ".format(symbol, price)
print (btc_price)

api =  os.environ.get('Kavenegar_API') #add as os env
#params = { 'sender' : '2000500666', 'receptor': '0918370***', 'message' : message }
#response = api.sms_send( params)



#using file arg1 arg2 arg3
data = 'receptor=' + str(sys.argv[1])  + '&' + 'token=BNBUSDT' + '&' + 'token2=' + price + '&' + 'template=symb'
url="https://api.kavenegar.com/v1/" +  api + "/verify/lookup.json?" + data
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#r = requests.post(url, headers=headers)
