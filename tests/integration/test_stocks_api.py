import time
import threading
import unittest.main

import requests
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
        #server_thread.start()

        avapi.API_ENDPOINT = 'http://127.0.0.1:5000/query'

        max_time = 5
        time_elapsed = 0
        start_time = time.time()

        # if test server not started in 5 seconds then let the
        # test script die
        while time_elapsed < max_time:
            try:
                requests.get(avapi.API_ENDPOINT, timeout=1)
                break
            except:
                time_elapsed = time.time() - start_time

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