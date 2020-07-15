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
        """ Get basic financial data on a company.

        Args:
            symbol (str): The symbol for the target stock.
            metric (str): Metrics to retrieve. Can be one of
                all, price, valuation, margin.

        Returns:
            str: A json string containing company financial data.
        """

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
        """ Get financials as reported for a company.
        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing company financials
                as reported data.
        """

        endpoint = 'stock/financials-reported'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_filings(self, symbol):
        """ Get company filings. Limited to 250 documents at a
        time.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing company filing data.
        """
        endpoint = 'stock/filings'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_ipo_calendar(self, start, end):
        """ Get recent and upcoming IPOs.

        Args:
            start (str): The start date in the form YYYY-DD-MM.
            end (str): The end date in the form YYYY-DD-MM

        Returns:
            str: A json string containing IPO calendar data.
        """
        endpoint = 'calendar/ipo'
        params = {'from': start, 'to': end}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_recommendation_trends(self, symbol):
        """ Get latest analyst recommendation trends for
        a company.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing recommendation trend
                data.
        """
        endpoint = 'stock/recommendation'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_price_target(self, symbol):
        """ Get latests price target consensus.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing price target data.
        """
        endpoint = 'stock/price-target'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_eps_surprises(self, symbol):
        """ Get historic quarterly eps surprises.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing eps surprise data.
        """
        endpoint = 'stock/earnings'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_earnings_calendar(self, symbol):
        """ Get historical and upcoming earnings data.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing earnings calendar data.
        """
        endpoint = 'calendar/earnings'
        params = {'symbol': symbol, 'international': True}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_quote(self, symbol):
        """ Get real time quotes for a stock. US stocks only.

        Args:
            symbol (str): The symbol for the target stock.

        Returns:
            str: A json string containing quote data.
        """
        endpoint = 'quote'
        params = {'symbol': symbol}
        response = self._session.get(
            self.API_URL + endpoint,
            params=params
        )
        return response.text

    def get_candles(self, symbol, interval, start, end, adjusted=False):
        """ Get candlestick data for a company.

        Args:
            symbol (str): The symbol for the target stock.
            interval (str): candlestick size. can be 1, 5, 15, 30 or 60 mins
                or daily (D), weekly (w), monthly (m).
            start (int): unix timestamp of the start date.
            end (int): unix timestamp of the end date.
            adjusted (bool): True for adjusted data, False otherwise.

        Returns:
            str: A json string containing candlestick data.
        """
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
        """ Get splits for a stock.

        Args:
            symbol (str): The symbol for the target stock.
            start (str): The start date in the form YYYY-MM-DD
            end (str): The end date in the form YYYY-MM-DD

        Returns:
            str: A json string containing splits data.
        """
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
        """ Identifies candlestick patterns for a stock

        Args:
            symbol (str): The symbol for the target stock.
            interval (str): The candlestick size. One of 1,
                5, 15, 30, 60, D, W, M

        Returns:
            str: A json string containing pattern data.
        """
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
        """ Get support and resistance levels for a stock.

        Args:
            symbol (str): The symbol for the target stock.
            interval (str): The candlestick size. One of 1,
                5, 15, 30, 60, D, W, M

        Returns:
            str: A json string containing support and resistance
                data.
        """
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
        """ Get the aggregate signal of multiple technical
        indicators.

        Args:
            symbol (str): The symbol for the target stock.
            interval (str): The candlestick size. One of 1,
                5, 15, 30, 60, D, W, M

        Returns:
            str: A json string containing aggregate signal
                data.
        """
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