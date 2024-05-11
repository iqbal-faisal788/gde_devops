import requests
from logs import logger
import config as cfg

class getQuote():
    def __init__(self, symbol):
        # load confiugration
        self.config = cfg.get_config()
        self.symbol = symbol
        # self.error = None
        self.quote = self.get_quote()
        #del self.weather['Credits']
        #del self.weather['Code']
        logger.info(f'Quote for {self.symbol} retrieved')
        
        
    def get_quote(self):
        logger.debug(f'Getting quote for {self.symbol}')
        querystring = {"symbol":self.symbol}
        headers = {
            "X-RapidAPI-Key": self.config['stock_api']['rapidapi_key'],
            "X-RapidAPI-Host": self.config['stock_api']['rapidapi_host']
        }
        c = self.config['stock_api']['url']
        response = requests.get(self.config['stock_api']['url'], headers=headers, params=querystring)
        return response.json()

    def verbal_quote(self):
        message = ({"Company":{self.quote["name"]}, "Date": {self.quote["datetime"]}, "Closing Price":{self.quote["close"]}, "Volume": {self.quote["volume"]} })
        logger.debug(f'Verbose message requested for {self.quote}')
        logger.debug(message)
        return message

    #test case for single attribute
    def company(self):
        logger.debug(f'Company name for {self.quote}')
        return {self.quote["name"]}

    def date(self):
        logger.debug(f'Date for {self.quote}')
        return {self.quote["datetime"]}

    def closing_price(self):
        logger.debug(f'Closing price for {self.quote}')
        return {self.quote["close"]}
    
    def volume(self):
        logger.debug(f'Volume traded for {self.quote}')
        return {self.quote["volume"]}


    #test case for entire payload
    def quote_report(self):
        return self.quote
    
#obj = getQuote("AMZN")
#print(obj.verbal_quote())
#print(obj.company())
#works print(obj.get_quote())
#print(obj.quote_report())