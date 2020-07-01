import unittest
from unittest import mock
from finpy import yahoo as yh

class TestStocksClient(unittest.TestCase):
    def setUp(self):
        req_path = 'finpy.yahoo.stocks.requests.Session.get'
        self.mock_get_patcher = mock.patch(req_path)
        self.mock_get = self.mock_get_patcher.start()
        self.mock_get.return_value.text = r'{"some":"json"}'

        mock_key = '0000000000'
        self.client = yh.stocks.Client(mock_key)

    def test_get_earnings_history(self):
        """ test that a valid earnings history request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_earnings_history('MSFT')
        self.assertEqual(data, expected)

    def test_get_insider_holders(self):
        """ test that a valid insider holders request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_insider_holders('MSFT')
        self.assertEqual(data, expected)

    def test_get_history_with_default_interval(self):
        """ test that a valid history request will return
        data using the default interval (1 day). """

        expected = self.mock_get.return_value.text
        data = self.client.get_history('MSFT')
        self.assertEqual(data, expected)

    def test_get_history_with_valid_interval_str(self):
        """ test that a valid history request will return
        data if a valid interval str arg is provided. """

        expected = self.mock_get.return_value.text
        data = self.client.get_history('MSFT', interval='15m')
        self.assertEqual(data, expected)

    def test_get_history_with_valid_interval_enum(self):
        """ test that a valid history request will return
        data if a valid interval enum arg is provided. """

        expected = self.mock_get.return_value.text
        data = self.client.get_history(
            'MSFT',
            interval=yh.stocks.Interval.M5
        )
        self.assertEqual(data, expected)

    def test_get_history_with_invalid_interval_arg(self):
        """ test that an invalid history request will raise
        a value error if an invalid interval str arg is
        provided. """

        with self.assertRaises(ValueError):
            data = self.client.get_history(
                'MSFT',
                interval='1s'
            )

    def test_get_financial_data(self):
        """ test that a valid financial data request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_financial_data('MSFT')
        self.assertEqual(data, expected)

    def test_get_cashflow_statement(self):
        """ test that a valid cashflow statement request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_cashflow_statement('MSFT')
        self.assertEqual(data, expected)

    def test_get_insider_transactions(self):
        """ test that a valid insider transactions request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_insider_transactions('MSFT')
        self.assertEqual(data, expected)

    def test_get_profile(self):
        """ test that a valid profile request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_profile('MSFT')
        self.assertEqual(data, expected)

    def test_get_sec_filings(self):
        """ test that a valid sec filings request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_sec_filings('MSFT')
        self.assertEqual(data, expected)

    def test_get_calendar_events(self):
        """ test that a valid calendar events request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_calendar_events('MSFT')
        self.assertEqual(data, expected)

    def test_get_index_trend(self):
        """ test that a valid index trend request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_index_trend('MSFT')
        self.assertEqual(data, expected)

    def test_get_earnings_trend(self):
        """ test that a valid earnings trend request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_earnings_trend('MSFT')
        self.assertEqual(data, expected)

    def test_get_key_statistics(self):
        """ test that a valid key statistics request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_key_statistics('MSFT')
        self.assertEqual(data, expected)

    def test_get_earnings(self):
        """ test that a valid earnings request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_earnings('MSFT')
        self.assertEqual(data, expected)

    def test_get_net_share_purchase_activity(self):
        """ test that a valid net share purchase activity
        request will return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_net_share_purchase_activity('MSFT')
        self.assertEqual(data, expected)

    def test_get_upgrade_downgrade_history(self):
        """ test that a valid upgrade downgrade history
        request will return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_upgrade_downgrade_history('MSFT')
        self.assertEqual(data, expected)

    def test_get_institution_ownership(self):
        """ test that a valid institution ownership
        request will return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_institution_ownership('MSFT')
        self.assertEqual(data, expected)

    def test_get_recommendation_trend(self):
        """ test that a valid recommendation trend
        request will return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_recommendation_trend('MSFT')
        self.assertEqual(data, expected)

    def test_get_balance_sheet(self):
        """ test that a valid balance sheet request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_balance_sheet('MSFT')
        self.assertEqual(data, expected)