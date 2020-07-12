import requests

class StockClient():
    """ A client for the finnhub stock api.
    Provides technical and fundamental data on stock
    symbols.

    Args:
        api_key (str): A finnhub api key.
    """
    API_URL = 'https://finnhub.io/api/v1/'

    def __init__(self, api_key):
        self._session = requests.Session()
        self._session.headers = {'X-Finnhub-Token': api_key}

    def get_profile(self, symbol):
        """ Get general information for a company.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing company profile data.
        """
        endpoint = 'stock/profile2'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_symbols(self, exchange):
        """ Lists supported company symbols.

        Args:
            exchange (str): The exchange to list supported
                symbols from.

        Returns:
            str: A json string containing a list of symbols from
                the provided exchange.
        """
        endpoint = 'stock/symbol'
        params = {'exchange': exchange}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_market_news(self, category='general'):
        """ Get the latest market news for the provided category.

        Args:
            category (str): Category of the news to be retrieved.
                Can be one of general, forex, crypto or merger.


        Returns:
            str: A json string containing news from the provided
                category.
        """
        endpoint = 'news'
        params = {'category': category}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_news(self, symbol, start, end):
        """ Get latest news for the provided company symbol.
        North American companies only.

        Args:
            symbol (str): The symbol for the target stock.
            start (str): Oldest date to retrieve news from. Must
                be of the form YYYY-MM-DD.
            end (str): Most recent date to retrieve news to. Must
                be of the form YYYY-MM-DD

        Returns:
            str: A json string containing company news data.
        """
        endpoint = 'company-news'
        params = {
            'symbol': symbol,
            'from': start,
            'to': end
        }
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_news_sentiment(self, symbol):
        """ Get news sentiment and statistics for a company.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing company news sentiment data.
        """
        endpoint = 'news-sentiment'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_peers(self, symbol):
        """ Get peers for a company. These are companies in
        the same country and GICS sub-industry as the target
        symbol.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing company peers data.
        """
        endpoint = 'stock/peers'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_basic_financials(self, symbol, metric='all'):
        endpoint = 'stock/metric'
        params = {
            'symbol': symbol,
            'metric': metric
        }
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_financials_as_reported(self, symbol):
        endpoint = 'stock/financials-reported'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_filings(self, symbol):
        endpoint = 'stock/filings'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_ipo_calendar(self, start, end):
        endpoint = 'calendar/ipo'
        params = {'from': start, 'to': end}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_recommendation_trends(self, symbol):
        endpoint = 'stock/recommendation'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_price_target(self, symbol):
        endpoint = 'stock/price-target'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_eps_surprises(self, symbol):
        endpoint = 'stock/earnings'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_earnings_calendar(self, symbol):
        endpoint = 'calendar/earnings'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_quote(self, symbol):
        endpoint = 'quote'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_candles(self, symbol, interval, start, end, adjusted=False):
        endpoint = 'stock/candle'
        params = {
            'symbol': symbol,
            'resolution': interval,
            'from': start,
            'to': end
        }
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_splits(self, symbol, start, end):
        endpoint = 'stock/split'
        params = {
            'symbol': symbol,
            'from': start,
            'to': end
        }
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_patterns(self, symbol, interval):
        endpoint = 'scan/pattern'
        params = {
            'symbol': symbol,
            'resolution': interval,
        }
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_support_resistance(self, symbol, interval):
        endpoint = 'scan/support-resistance'
        params = {
            'symbol': symbol,
            'resolution': interval
        }
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_aggregate_signal(self, symbol, interval):
        endpoint = 'scan/technical-indicator'
        params = {
            'symbol': symbol,
            'resolution': interval
        }
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_indicator(self, symbol, interval, start, end, indicator, indicator_fields={}):
        endpoint = 'indicator'
        params = {
            'symbol': symbol,
            'resolution': interval,
            'from': start,
            'to': end,
            'indicator': indicator
        }
        params.update(indicator_fields)
        print(params)
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text