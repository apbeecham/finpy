import time
import threading
import unittest.main

import requests
from finpy import alphavantage as av
from tests.fixtures import av_test_server

class TestStockClient(unittest.TestCase):
    """ Integration Test cases for the alphavantage stock price
    client. """

    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(
            target=av_test_server.app.run,
            kwargs={'port':5000}
        )
        cls.server_thread.setDaemon(True)
        cls.server_thread.start()

        av.StockClient.API_URL = 'http://127.0.0.1:5000/query'

        max_time = 5
        time_elapsed = 0
        start_time = time.time()
        # if test server not started in 5 seconds then run the
        # test suite anyway...
        while time_elapsed < max_time:
            try:
                requests.get(av.StockClient.API_URL, timeout=1)
                break
            except:
                time_elapsed = time.time() - start_time

    def setUp(self):
        api_key = '0000000000'
        self.client = av.StockClient(api_key)

    def test_get_intraday_request(self):
        """ Test that a request successfully retrieves data if a
        valid intraday request is made. """

        data = self.client.get_intraday_data('MSFT')
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

    def test_get_daily_request(self):
        """ Test that a request successfully retrieves data if a
        valid daily request is made."""

        data = self.client.get_daily_data('MSFT')
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

    def test_get_daily_adjusted_request(self):
        """ Test that a request successfully retrieves data if a
        valid daily adjusted request is made."""

        data = self.client.get_daily_adjusted_data('MSFT')
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

if __name__ == '__main__':
    unittest.main()