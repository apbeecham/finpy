import unittest
from unittest import TestCase
from alphavantage import api as avapi
from alphavantage.api import StocksAPI, Interval, OutputSize, DataType

class TestRequests(TestCase):
    def setUp(self):
        avapi.API_ENDPOINT = 'http://127.0.0.1:5000/query'
        api_key = '0000000000'
        self.api = StocksAPI(api_key)

    def test_get_intraday_request(self):
        data = self.api.get_intraday_data('MSFT')
        print(data)
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

    def test_get_daily_request(self):
        data = self.api.get_daily_data('MSFT')
        print(data)
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

    def test_get_daily_adjusted_request(self):
        data = self.api.get_daily_adjusted_data('MSFT')
        print(data)
        self.assertIsNotNone(data)
        self.assertNotIn(data,['forbidden','invalid parameters','not found'])

if __name__ == '__main__':
    unittest.main()