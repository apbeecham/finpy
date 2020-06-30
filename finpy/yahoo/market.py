import requests

class Client:
    """ A client for the yahoo market api yahoo.
    Provides market news and stats.

    Args:
        api_key (str): A yahoo api key.
    """

    API_URL = 'https://yahoo-finance15.p.rapidapi.com/api/yahoo/'

    def __init__(self, api_key):
        self._session = requests.Session()

        self._session.headers = {
            'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
            'x-rapidapi-key': api_key
        }

    def get_mutual_funds(self):
        """ Request mutual funds ordered by most gains in today's market.

        Returns:
            str: A json string containing mutual funds ordered by most
                gains in today's market.
        """
        end_point = 'mu/topmutualfunds'
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_top_gainers(self):
        """ Request stocks with the most gains in today's market.

        Returns:
            str: A json string containing stocks with the most gains
                in today's market.
        """
        end_point = 'ga/topgainers'
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_most_watched(self):
        """ Request trending stocks in today's market.

        Returns:
            str: A json string containing trending stocks in
                today's market.
        """
        end_point = 'tr/trending'
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_news(self, symbol):
        """ Request recently published news for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing recently published news for
                the provided symbol.
        """

        end_point = 'tr/trending'
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_quotes(self, symbols):
        """ Request quote data for stocks, etfs, mutual funds and more.

        Args:
            symbols (array): array of symbol for each target security.

        Returns:
            str: A json string containing quote data for
                the provided symbols.
        """
        sym_str = ','.join(symbols)
        end_point = 'qu/quote/{}'.format(sym_str)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_etfs(self):
        """ Request ETFs ordered by most gains in today's market.

        Returns:
            str: A json string containing ETFs ordered by most
                gains in today's market.
        """
        end_point = 'et/topetfs'
        response = self._session.get(self.API_URL + end_point)
        return response.text
