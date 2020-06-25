import unittest
from unittest import mock
from finpy.alphavantage import api as avapi

class TestStocksApi(unittest.TestCase):
    def setUp(self):
        req_path = 'finpy.alphavantage.api.requests.Session.get'
        self.mock_get_patcher = mock.patch(req_path)
        self.mock_get = self.mock_get_patcher.start()
        self.mock_get.return_value.text = r'{"some":"json"}'

        mock_key = '0000000000'
        self.api = avapi.StocksAPI(mock_key)

    def test_get_intraday_with_default_params(self):
        """ test that a valid intraday request with
        default kwargs returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_intraday_data('MSFT')
        self.assertEqual(data, expected)

    def test_get_daily_with_default_params(self):
        """ test that a valid daily request with
        default kwargs returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_daily_data('MSFT')
        self.assertEqual(data, expected)

    def test_get_daily_adjusted_with_default_params(self):
        """ test that a valid daily adjusted request with
        default kwargs returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_daily_adjusted_data('MSFT')
        self.assertEqual(data, expected)

    def test_get_intraday_with_str_params(self):
        """ test that a valid intraday request with
        string args returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_intraday_data(
            'MSFT',
            interval='5min',
            output_size='full',
            data_type='csv'
        )
        self.assertEqual(data, expected)

    def test_get_daily_with_str_params(self):
        """ test that a valid daily request with
        string args returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_daily_data(
            'MSFT',
            output_size='full',
            data_type='csv'
        )
        self.assertEqual(data, expected)

    def test_get_daily_adjusted_with_str_params(self):
        """ test that a valid daily adjusted request with
        string args returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_daily_adjusted_data(
            'MSFT',
            output_size='full',
            data_type='csv'
        )
        self.assertEqual(data, expected)

    def test_get_intraday_with_enum_params(self):
        """ test that a valid intraday request with
        enum args returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_intraday_data(
            'MSFT',
            interval=avapi.Interval.M1,
            output_size=avapi.OutputSize.FULL,
            data_type=avapi.DataType.CSV
        )
        self.assertEqual(data, expected)

    def test_get_daily_with_enum_params(self):
        """ test that a valid daily request with
        string args returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_daily_data(
            'MSFT',
            output_size=avapi.OutputSize.FULL,
            data_type=avapi.DataType.CSV
        )
        self.assertEqual(data, expected)

    def test_get_daily_adjusted_with_enum_params(self):
        """ test that a valid daily adjusted request with
        string args returns data. """

        expected = self.mock_get.return_value.text
        data = self.api.get_daily_adjusted_data(
            'MSFT',
            output_size=avapi.OutputSize.FULL,
            data_type=avapi.DataType.CSV
        )
        self.assertEqual(data, expected)

    def test_get_intraday_with_invalid_params(self):
        """ test that invalid intraday requests raise
        value errors. """

        with self.assertRaises(ValueError):
            self.api.get_intraday_data('MSFT', interval='2min')
        with self.assertRaises(ValueError):
            self.api.get_intraday_data('MSFT', output_size='big')
        with self.assertRaises(ValueError):
            self.api.get_intraday_data('MSFT', data_type='xml')

    def test_get_daily_with_invalid_params(self):
        """ test that invalid daily requests raise
        value errors. """

        with self.assertRaises(ValueError):
            self.api.get_daily_data('MSFT', output_size='big')
        with self.assertRaises(ValueError):
            self.api.get_daily_data('MSFT', data_type='xml')

    def test_get_daily_adjusted_with_invalid_params(self):
        """ test that invalid daily adjusted requests raise
        value errors. """

        with self.assertRaises(ValueError):
            self.api.get_daily_adjusted_data('MSFT', output_size='big')
        with self.assertRaises(ValueError):
            self.api.get_daily_adjusted_data('MSFT', data_type='xml')

    def tearDown(self):
        self.mock_get_patcher.stop()

if __name__ == '__main__':
    unittest.main()