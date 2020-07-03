"""
Alphavantage financial data client and utilities.
"""
import enum

import requests

API_URL = 'https://www.alphavantage.co/query'

class Interval(enum.Enum):
    """ Possible interval values for intraday requests. """

    M1 = '1min'
    M5 = '5min'
    M15 = '15min'
    M30 = '30min'
    H1 = '60min'

    def __str__(self):
        return self.value

class OutputSize(enum.Enum):
    """ Output sizes of api responses. Use'full' for the full
    history or compact for the last 100 data points.
    """

    FULL = 'full'
    COMPACT = 'compact'

    def __str__(self):
        return self.value

class DataType(enum.Enum):
    """ Available Formats for data returned from the api.
    Either 'csv' or 'json'.
    """

    CSV = 'csv'
    JSON = 'json'

    def __str__(self):
        return self.value

class Function(enum.Enum):
    """ The API function to use when making a request. Specifies
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

class StockClient:
    """ A client for the Stock Time Series functions provided by
    the AlphaVantage REST API.

    Args:
        api_key (str): An alpha vantage api key.
    """

    def __init__(self, api_key):
        self._session = requests.Session()
        self._session.params['apikey'] = api_key

    def get_intraday_data(
                self,
                symbol,
                interval=Interval.H1,
                output_size=OutputSize.COMPACT,
                data_type=DataType.JSON
            ):
        """ Requests intraday stock price time series data.

        Args:
            symbol (str): The symbol of the stock to retrieve data for.
            interval (str): The granularity of the returned time series data.
            output_size (str): The size of the output data. Either full for
                the entire history of the symbol or compact for the last 100
                entries.
            data_type (str): The format of the returned price data. either csv
            or json.
        Returns:
            str: The body of the response from the api.
        """

        params = {
            'function': Function.INTRADAY,
            'symbol': symbol,
            'interval': Interval(interval),
        }

        response = self._handle_request(params, output_size, data_type)
        return response.text

    def get_daily_data(
                self,
                symbol,
                output_size=OutputSize.COMPACT,
                data_type=DataType.JSON
            ):

        """ Requests daily stock price time series data.

        Args:
            symbol (str): The symbol of the stock to retrieve data for.
            output_size (str): The size of the output data. Either full for
                the entire history of the symbol or compact for the last 100
                entries.
            data_type (str): The format of the returned price data. either csv
                or json.
        Returns:
            str: The body of the response from the api.
        """

        params = {
            'function': Function.DAILY,
            'symbol': symbol
        }

        response = self._handle_request(params, output_size, data_type)
        return response.text

    def get_daily_adjusted_data(
                self,
                symbol,
                output_size=OutputSize.COMPACT,
                data_type=DataType.JSON
            ):
        """ Requests daily adjusted stock price time series data.

        Args:
            symbol (str): The symbol of the stock to retrieve data for.
            output_size (str): The size of the output data. Either full for
                the entire history of the symbol or compact for the last 100
                entries.
            data_type (str): The format of the returned price data. either csv
                or json.
        Returns:
            str: The body of the response from the api.
        """

        params = {
            'function': Function.DAILY_ADJUSTED,
            'symbol': symbol
        }

        response = self._handle_request(params, output_size, data_type)
        return response.text

    def _handle_request(self, params, output_size, data_type):
        # request equity data
        params['outputsize'] = OutputSize(output_size)
        params['datatype'] = DataType(data_type)
        return self._session.get(API_URL, params=params)
