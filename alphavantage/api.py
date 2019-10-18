import requests

from enum import Enum

API_ENDPOINT = 'https://www.alphavantage.co/query'

class Interval(Enum):
    M1  = '1min'
    M5  = '5min'
    M15 = '15min'
    M30 = '30min'
    H1  = '60min'

    def __str__(self):
        return self.value

class OutputSize(Enum):
    FULL    = 'full'
    COMPACT = 'compact'

    def __str__(self):
        return self.value

class DataType(Enum):
    CSV     = 'csv'
    JSON    = 'json'

    def __str__(self):
        return self.value

class Function(Enum):
    QUOTE               = 'GLOBAL_QUOTE'
    SEARCH              = 'SYMBOL_SEARCH'
    INTRADAY            = 'TIME_SERIES_INTRADAY'
    DAILY               = 'TIME_SERIES_DAILY'
    DAILY_ADJUSTED      = 'TIME_SERIES_DAILY_ADJUSTED'
    WEEKLY              = 'TIME_SERIES_WEEKLY'
    WEEKLY_ADJUSTED     = 'TIME_SERIES_WEEKLY_ADJUSTED'
    MONTHLY             = 'TIME_SERIES_MONTHLY'
    MONTHLY_ADJUSTED    = 'TIME_SERIES_MONTHLY_ADJUSTED'

    def __str__(self):
        return self.value    

class StocksAPI():
    def __init__(self, api_key):
        self._api_key = api_key

    def get_intraday_data(self, symbol, interval=Interval.H1, output_size=OutputSize.COMPACT, data_type=DataType.JSON):
        interval = Interval(interval)
        output_size = OutputSize(output_size)
        data_type = DataType(data_type)

        params = {
            'function': Function.INTRADAY,
            'symbol': symbol,
            'interval': interval,
            'outputsize': output_size,
            'datatype': data_type,
            'apikey': self._api_key
        }

        response = requests.get(API_ENDPOINT, params=params)
        return response.text

    def get_daily_data(self, symbol, output_size=OutputSize.COMPACT, data_type=DataType.JSON):
        output_size = OutputSize(output_size)
        data_type = DataType(data_type)

        params = {
            'function': Function.DAILY,
            'symbol': symbol,
            'outputsize':output_size,
            'datatype':data_type,
            'apikey':self._api_key
        }

        response = requests.get(API_ENDPOINT, params=params)
        return response.text

    def get_daily_adjusted_data(self, symbol, output_size=OutputSize.COMPACT, data_type=DataType.JSON):
        output_size = OutputSize(output_size)
        data_type = DataType(data_type)

        params = {
            'function': Function.DAILY_ADJUSTED,
            'symbol': symbol,
            'outputsize':output_size,
            'datatype':data_type,
            'apikey':self._api_key
        }

        response = requests.get(API_ENDPOINT, params=params)
        return response.text
        
        
