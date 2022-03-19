import requests
#from flask import Flask
#from flask_restful import Resource, Api, reqparse
#import pandas as pd
#import ast
#app = Flask(__name__)
#api = Api(app)




API_KEY = '64TY7285TUX7FM6P'

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=' + API_KEY)
if (r.status_code == 200):
  print r.json()
result = r.json()

dataForAllDays = result['Time Series (Daily)']
dataForSingleDate = dataForAllDays['2017-10-30']

print dataForSingleDate['1. open']
print dataForSingleDate['2. high']
print dataForSingleDate['3. low']
print dataForSingleDate['4. close']
print dataForSingleDate['5. volume']