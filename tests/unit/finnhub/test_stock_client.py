import datetime
import unittest
from unittest import mock
from finpy import finnhub as fh

class TestStockClient(unittest.TestCase):
    def setUp(self):
        req_path = 'finpy.yahoo.requests.Session.get'
        self.mock_get_patcher = mock.patch(req_path)
        self.mock_get = self.mock_get_patcher.start()
        self.mock_get.return_value.text = r'{"some":"json"}'

        mock_key = '0000000000'
        self.client = fh.StockClient(mock_key)

    def test_get_profile(self):
        """ test that a valid profile request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_profile('MSFT')
        self.assertEqual(data, expected)


    def test_get_symbols(self):
        """ test that a valid symbols request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_symbols('LSE')
        self.assertEqual(data, expected)

    def test_get_market_news(self):
        """ test that a valid market news request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_market_news()
        self.assertEqual(data, expected)

    def test_get_news(self):
        """ test that a valid news request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_news('MSFT', '2020-01-01', '2020-01-31')
        self.assertEqual(data, expected)

    def test_get_news_sentiment(self):
        """ test that a valid news sentiment request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_news_sentiment('MSFT')
        self.assertEqual(data, expected)

    def test_get_peers(self):
        """ test that a valid peers request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_peers('MSFT')
        self.assertEqual(data, expected)

    def test_get_basic_financials(self):
        """ test that a valid basic financials request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_basic_financials('MSFT')
        self.assertEqual(data, expected)

    def test_get_financials_as_reported(self):
        """ test that a valid financials as reported request
        will return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_financials_as_reported('MSFT')
        self.assertEqual(data, expected)

    def test_get_filings(self):
        """ test that a valid filings request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_filings('MSFT')
        self.assertEqual(data, expected)


    def test_get_ipo_calendar(self):
        """ test that a valid profile request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_ipo_calendar('2020-01-01', '2020-01-31')
        self.assertEqual(data, expected)

    def test_get_recommendation_trends(self):
        """ test that a valid recommendation trends request
        will return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_recommendation_trends('MSFT')
        self.assertEqual(data, expected)

    def test_get_price_target(self):
        """ test that a valid price target request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_price_target('MSFT')
        self.assertEqual(data, expected)

    def test_get_eps_surprises(self):
        """ test that a valid eps surprises request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_eps_surprises('MSFT')
        self.assertEqual(data, expected)

    def test_get_earnings_calendar(self):
        """ test that a valid earnings calendar request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_earnings_calendar('MSFT')
        self.assertEqual(data, expected)

    def test_get_quote(self):
        """ test that a valid quote request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_quote('MSFT')
        self.assertEqual(data, expected)

    def test_get_candles(self):
        """ test that a valid candles request will
        return data. """

        expected = self.mock_get.return_value.text
        start = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
        end = datetime.datetime.strptime('2020-01-31', '%Y-%m-%d')
        data = self.client.get_candles(
            'MSFT',
            'D',
            int(start.timestamp()),
            int(end.timestamp())
        )
        self.assertEqual(data, expected)

    def test_get_splits(self):
        """ test that a valid splits request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_splits('MSFT', '2020-01-01', '2020-01-31')
        self.assertEqual(data, expected)


    def test_get_patterns(self):
        """ test that a valid patterns request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_patterns('MSFT', 'D')
        self.assertEqual(data, expected)


    def test_get_support_resistance(self):
        """ test that a valid support resistance request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_support_resistance('MSFT', 'D')
        self.assertEqual(data, expected)


    def test_get_aggregate_signal(self):
        """ test that a valid quote request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_aggregate_signal('MSFT', 'D')
        self.assertEqual(data, expected)
