# import os
# import json
# from django.conf import settings
# from django.shortcuts import render, redirect, get_object_or_404
# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# from django.shortcuts import render
# from .models import Coin


# tickerList = []
# URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# params = {
#     'start': '1',
#     'limit': '10',
#     'convert': 'USD'
# }

# headers = {
#     'X-CMC_PRO_API_KEY': settings.APIKEY,
#     'Accepts': 'application/json'
# }

# session = Session()
# session.headers.update(headers)


# def call_api():
#     try:
#         response = session.get(URL, params=params)
#         data = json.loads(response.text)
#         coins = data['data']
#         get_ticker_list(data)
#         print("You work?")

#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)


# def get_ticker_list(data):
#     for d in data['data']:
#         ticker_from_api = d['symbol']
#         tickerList.append(ticker_from_api)
    
#     print(tickerList)


# def validate_ticker(ticker):
#     """
#     Will validate if the users ticker exits in tickerList
#     """
#     for x in tickerList:

#         if ticker in tickerList:
#             return True

#         else:
#             return False

        
# def validate_amount(amount):
#     """
#     Will validate is the users coin amount to ensure only contains numbers
#     """
#     try:
#         amount = float(amount)
#         return True

#     except ValueError:
#         return False


# def display_coin_data(ticker, data):
#     """
#     Will display relevant data that user asks for
#     """

#     if ticker in tickerList:
#         for x in coins:
#             if x['symbol'] == ticker:
#                 coin_data = (x['symbol'], x['quote']['USD'][data])
    
#         return coin_data
    
#     else:
#         print("Ticker not in List")


# def get_coin_price(ticker):
#     if ticker in tickerList:
#         print("Success")
#         for x in coins:
#             if x['symbol'] == ticker:
#                 price = float((x['quote']['USD']['price']))

#         return price