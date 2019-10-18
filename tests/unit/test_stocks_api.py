import unittest
from unittest import TestCase
from unittest.mock import Mock, patch
from alphavantage.api import StocksAPI, Interval, OutputSize, DataType

class TestStocksApi(TestCase):
    def setUp(self):
        self.mock_get_patcher = patch('alphavantage.api.requests.get')
        self.mock_get = self.mock_get_patcher.start()
        self.mock_get.return_value.text = r'{"some":"json"}'

        mock_key = '0000000000'
        self.api = StocksAPI(mock_key)

    def test_get_intraday_with_default_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_intraday_data('MSFT')
        self.assertEqual(data, expected)

    def test_get_daily_with_default_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_daily_data('MSFT')
        self.assertEqual(data, expected)

    def test_get_daily_adjusted_with_default_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_daily_adjusted_data('MSFT')
        self.assertEqual(data, expected)

    def test_get_intraday_with_str_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_intraday_data(
            'MSFT', 
            interval='5min', 
            output_size='full', 
            data_type='csv'
        )
        self.assertEqual(data, expected)

    def test_get_daily_with_str_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_daily_data(
            'MSFT', 
            output_size='full', 
            data_type='csv'
        )
        self.assertEqual(data, expected)

    def test_get_daily_adjusted_with_str_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_daily_adjusted_data(
            'MSFT', 
            output_size='full', 
            data_type='csv'
        )
        self.assertEqual(data, expected)

    def test_get_intraday_with_enum_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_intraday_data(
            'MSFT', 
            interval=Interval.M1, 
            output_size=OutputSize.FULL, 
            data_type=DataType.CSV
        )
        self.assertEqual(data, expected)

    def test_get_daily_with_enum_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_daily_data(
            'MSFT', 
            output_size=OutputSize.FULL, 
            data_type=DataType.CSV
        )
        self.assertEqual(data, expected)

    def test_get_daily_adjusted_with_enum_params(self):
        expected = self.mock_get.return_value.text
        data = self.api.get_daily_adjusted_data(
            'MSFT', 
            output_size=OutputSize.FULL, 
            data_type=DataType.CSV
        )
        self.assertEqual(data, expected)

    def test_get_intraday_with_invalid_params(self):
        with self.assertRaises(ValueError):
            self.api.get_intraday_data('MSFT', interval='2min')
        with self.assertRaises(ValueError):
            self.api.get_intraday_data('MSFT', output_size='big')
        with self.assertRaises(ValueError):
            self.api.get_intraday_data('MSFT', data_type='xml')

    def test_get_daily_with_invalid_params(self):
        with self.assertRaises(ValueError):
            self.api.get_daily_data('MSFT', output_size='big')
        with self.assertRaises(ValueError):
            self.api.get_daily_data('MSFT', data_type='xml')

    def test_get_daily_adjusted_with_invalid_params(self):
        with self.assertRaises(ValueError):
            self.api.get_daily_adjusted_data('MSFT', output_size='big')
        with self.assertRaises(ValueError):
            self.api.get_daily_adjusted_data('MSFT', data_type='xml')

    def tearDown(self):
        self.mock_get_patcher.stop()

if __name__ == '__main__':
    unittest.main()