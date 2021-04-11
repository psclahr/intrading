import requests
import json
import os

def getHeaders() -> dict:
    return {
        'x-rapidapi-key': os.getenv('YAHOO_FINANCE_KEY'),
        'x-rapidapi-host': os.getenv('YAHOO_FINANCE_HOST')
    }


def actualDax() -> dict:
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region":"DE","symbols":"^GDAXI"}

    response = requests.request("GET", url, headers=getHeaders(), params=querystring)

    return json.loads(response.text)

def fetchChart(name: str, symbol: str) -> dict:
    filePath = 'data/' + name + '.json'

    try:
        with open(filePath, 'r') as file:
            return json.loads(file.read())
    except: 
        with open(filePath, 'x') as file:
            url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

            querystring = {"symbol": symbol,"interval":"1d","range":"5y","region":"DE"}

            response = requests.request("GET", url, headers=getHeaders(), params=querystring)

            file.write(response.text)

        with open(filePath, 'r') as file:
            return json.loads(file.read())

def historicalDax() -> dict:
    return fetchChart('dax', '^GDAXI')

def historicalEuroDollar() -> dict:
    return fetchChart('eur-usd', 'EURUSD=X')

def historicalBitcoinDollar() -> dict:
    return fetchChart('bitcoin-eur', 'BTC-EUR')
