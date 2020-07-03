import time
import threading
import unittest

import requests
from tests.fixtures import yh_test_server
from finpy import yahoo as yh

class TestMarketClient(unittest.TestCase):
    """ Integration Test cases for the yahoo market
    client. """

    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(
            target=yh_test_server.app.run,
            kwargs={'port':5002}
        )
        cls.server_thread.setDaemon(True)
        cls.server_thread.start()

        yh.market.Client.API_URL = 'http://127.0.0.1:5002/'

        max_time = 5
        time_elapsed = 0
        start_time = time.time()

        # if test server not started in 5 seconds then run the
        # test suite anyway...
        while time_elapsed < max_time:
            try:
                requests.get(yh.market.Client.API_URL, timeout=1)
                break
            except:
                time_elapsed = time.time() - start_time

    def setUp(self):
        api_key = '0000000000'
        self.client = yh.market.Client(api_key)

    def test_get_mutual_funds(self):
        """ Test that a request successfully retrieves data if a
        valid mutual funds request is made. """

        act_data = self.client.get_mutual_funds()
        with open('tests/fixtures/yh-responses/mutual-funds.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_top_gainers(self):
        """ Test that a request successfully retrieves data if a
        valid top gainers request is made. """

        act_data = self.client.get_top_gainers()
        with open('tests/fixtures/yh-responses/top-gainers.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_most_watched(self):
        """ Test that a request successfully retrieves data if a
        valid most watched request is made. """

        act_data = self.client.get_most_watched()
        with open('tests/fixtures/yh-responses/most-watched.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_news(self):
        """ Test that a request successfully retrieves data if a
        valid mutual funds request is made. """

        act_data = self.client.get_news('AAPL')
        with open('tests/fixtures/yh-responses/news.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_quote(self):
        """ Test that a request successfully retrieves data if a
        valid quote request is made. """

        act_data = self.client.get_quote(['AAPL'])
        with open('tests/fixtures/yh-responses/quote.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_etfs(self):
        """ Test that a request successfully retrieves data if a
        valid etfs request is made. """

        act_data = self.client.get_etfs()
        with open('tests/fixtures/yh-responses/etfs.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)