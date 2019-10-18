import unittest
from unittest import TestCase
from alphavantage.api import StocksAPI, Interval, OutputSize, DataType

class TestRequests(TestCase):
    def setUp(self):
        api_key = '0WCK07WURCWYKGHD'
        self.api = StocksAPI(api_key)

    def test_get_intraday_request(self):
        data = self.api.get_intraday_data('MSFT')
        self.assertIsNotNone(data)

    def test_get_daily_request(self):
        data = self.api.get_daily_data('MSFT')
        self.assertIsNotNone(data)

    def test_get_daily_adjusted_request(self):
        data = self.api.get_daily_adjusted_data('MSFT')
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()