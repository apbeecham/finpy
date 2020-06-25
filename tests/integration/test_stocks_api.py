import threading
import unittest.main

from finpy.alphavantage import api as avapi
from tests.integration import mock_api_server

class TestStocksAPI(unittest.TestCase):
    """ Integration Test cases for the alphavantage stock price
    api. """

    @classmethod
    def setUpClass(cls):
        server_thread = threading.Thread(
            group=None,
            target=mock_api_server.app.run
        )
        server_thread.setDaemon(True)
        server_thread.start()

        avapi.API_ENDPOINT = 'http://127.0.0.1:5000/query'

    def setUp(self):
        api_key = '0000000000'
        self.api = avapi.StocksAPI(api_key)

    def test_get_intraday_request(self):
        """ Test that a request successfully retrieves data if a
        valid intraday request is made. """

        data = self.api.get_intraday_data('MSFT')
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

    def test_get_daily_request(self):
        """ Test that a request successfully retrieves data if a
        valid daily request is made."""

        data = self.api.get_daily_data('MSFT')
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

    def test_get_daily_adjusted_request(self):
        """ Test that a request successfully retrieves data if a
        valid daily adjusted request is made."""

        data = self.api.get_daily_adjusted_data('MSFT')
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

if __name__ == '__main__':
    unittest.main()