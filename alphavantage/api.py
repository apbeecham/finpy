"""
A library of python wrapper classes for the Alpha Vantage API.

Attributes:
    API_ENDPOINT (str): the base url of the api
"""
from enum import Enum

import requests

API_ENDPOINT = 'https://www.alphavantage.co/query'

class Interval(Enum):
    """
    Possible interval values for intraday requests.
    """
    M1 = '1min'
    M5 = '5min'
    M15 = '15min'
    M30 = '30min'
    H1 = '60min'

    def __str__(self):
        return self.value

class OutputSize(Enum):
    """
    Output sizes of api responses.'full' for the full
    history or compact for the last 100 data points.
    """
    FULL = 'full'
    COMPACT = 'compact'

    def __str__(self):
        return self.value

class DataType(Enum):
    """
    Available Formats for data returned from the api.
    Either 'csv' or 'json'.
    """
    CSV = 'csv'
    JSON = 'json'

    def __str__(self):
        return self.value

class Function(Enum):
    """
    The API function to use when making a request. Specifies
    the granularity of the returned price data. 'GLOBAL_QUOTE'
    provides the current price data only. 'SYMBOL_SEARCH' allows
    searching for valid symbols.
    """
    QUOTE = 'GLOBAL_QUOTE'
    SEARCH = 'SYMBOL_SEARCH'
    INTRADAY = 'TIME_SERIES_INTRADAY'
    DAILY = 'TIME_SERIES_DAILY'
    WEEKLY = 'TIME_SERIES_WEEKLY'
    MONTHLY = 'TIME_SERIES_MONTHLY'
    DAILY_ADJUSTED = 'TIME_SERIES_DAILY_ADJUSTED'
    WEEKLY_ADJUSTED = 'TIME_SERIES_WEEKLY_ADJUSTED'
    MONTHLY_ADJUSTED = 'TIME_SERIES_MONTHLY_ADJUSTED'

    def __str__(self):
        return self.value

class StocksAPI():
    """
        A simple wrapper for the Stock Time Series functions provided by
        the Alpha Vantage REST API.

        Args:
            api_key (str): An alpha vantage api key.
    """
    def __init__(self, api_key):
        self._api_key = api_key

    def get_intraday_data(
            self,
            symbol,
            interval=Interval.H1,
            output_size=OutputSize.COMPACT,
            data_type=DataType.JSON
        ):
        """
        Requests intraday stock price time series data.

        Args:
            symbol (str): The symbol of the stock to retrieve data for.
            interval (str): The granularity of the returned time series data.
            can be one of :
                * 1min
                * 5min
                * 15min
                * 30min
                * 60min
            output_size (str): The size of the output data. Either full for
            the entire history of the symbol or compact for the last 100 entries.
            data_type (str): The format of the returned price data. either csv
            or json.
        Returns:
            (str) : The body of the response from the api.
        """
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
        """
        Requests daily stock price time series data.

        Args:
            symbol (str): The symbol of the stock to retrieve data for.
            output_size (str): The size of the output data. Either full for
            the entire history of the symbol or compact for the last 100 entries.
            data_type (str): The format of the returned price data. either csv
            or json.
        Returns:
            (str) : The body of the response from the api.
        """
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

    def get_daily_adjusted_data(
            self,
            symbol,
            output_size=OutputSize.COMPACT,
            data_type=DataType.JSON
        ):
        """
        Requests daily adjusted stock price time series data.

        Args:
            symbol (str): The symbol of the stock to retrieve data for.
            output_size (str): The size of the output data. Either full for
            the entire history of the symbol or compact for the last 100 entries.
            data_type (str): The format of the returned price data. either csv
            or json.
        Returns:
            (str) : The body of the response from the api.
        """
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
