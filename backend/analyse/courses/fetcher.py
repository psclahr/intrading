import requests
import os
import json

class Fetcher():
    def __getHeaders(self) -> dict:
        return {
            'x-rapidapi-key': os.getenv('YAHOO_FINANCE_KEY'),
            'x-rapidapi-host': os.getenv('YAHOO_FINANCE_HOST')
        }

    def getChart(self, name: str) -> dict:
        filePath = 'data/' + name + '.json'

        try:
            with open(filePath, 'r') as file:
                return json.loads(file.read())
        except: 
            with open(filePath, 'x') as file:
                url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

                querystring = {"symbol": '^GDAXI',"interval":"1d","range":"5y","region":"DE"}

                response = requests.request("GET", url, headers=self.__getHeaders(), params=querystring)

                file.write(response.text)

            with open(filePath, 'r') as file:
                return json.loads(file.read())