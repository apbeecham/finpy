import time
import threading
import unittest

import requests
from tests.fixtures import yh_test_server
from finpy import yahoo as yh

class TestStockClient(unittest.TestCase):
    """ Integration Test cases for the alphavantage stock price
    client. """

    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(
            target=yh_test_server.app.run,
            kwargs={'port':5001}
        )
        cls.server_thread.setDaemon(True)
        cls.server_thread.start()

        yh.stocks.Client.API_URL = 'http://127.0.0.1:5001/'

        max_time = 5
        time_elapsed = 0
        start_time = time.time()

        # if test server not started in 5 seconds then run the
        # test suite anyway...
        while time_elapsed < max_time:
            try:
                requests.get(yh.stocks.Client.API_URL, timeout=1)
                break
            except:
                time_elapsed = time.time() - start_time

    def setUp(self):
        api_key = '0000000000'
        self.client = yh.stocks.Client(api_key)

    def test_get_earnings_history(self):
        """ Test that a request successfully retrieves data if a
        valid earnings history request is made. """

        act_data = self.client.get_earnings_history('AAPL')
        with open('tests/fixtures/yh-responses/earnings-history.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_insider_holders(self):
        """ Test that a request successfully retrieves data if a
        valid insider holders request is made. """

        act_data = self.client.get_insider_holders('AAPL')
        with open('tests/fixtures/yh-responses/insider-holders.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_history(self):
        """ Test that a request successfully retrieves data if a
        valid history request is made. """

        act_data = self.client.get_history('AAPL')
        with open('tests/fixtures/yh-responses/history.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_financial_data(self):
        """ Test that a request successfully retrieves data if a
        valid financial data request is made. """

        act_data = self.client.get_financial_data('AAPL')
        with open('tests/fixtures/yh-responses/financial-data.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_cashflow_statement(self):
        """ Test that a request successfully retrieves data if a
        valid cashflow statement request is made. """

        act_data = self.client.get_cashflow_statement('AAPL')
        with open('tests/fixtures/yh-responses/cashflow-statement.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_insider_transactions(self):
        """ Test that a request successfully retrieves data if a
        valid insider transactions request is made. """

        act_data = self.client.get_insider_transactions('AAPL')
        with open('tests/fixtures/yh-responses/insider-transactions.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_profile(self):
        """ Test that a request successfully retrieves data if a
        valid profile request is made. """

        act_data = self.client.get_profile('AAPL')
        with open('tests/fixtures/yh-responses/profile.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_sec_filings(self):
        """ Test that a request successfully retrieves data if a
        valid sec filings request is made. """

        act_data = self.client.get_sec_filings('AAPL')
        with open('tests/fixtures/yh-responses/sec-filings.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_calendar_events(self):
        """ Test that a request successfully retrieves data if a
        valid calendar events request is made. """

        act_data = self.client.get_calendar_events('AAPL')
        with open('tests/fixtures/yh-responses/calendar-events.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_index_trend(self):
        """ Test that a request successfully retrieves data if a
        valid index trend request is made. """

        act_data = self.client.get_index_trend('AAPL')
        with open('tests/fixtures/yh-responses/index-trend.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_earnings_trend(self):
        """ Test that a request successfully retrieves data if a
        valid earnings trend request is made. """

        act_data = self.client.get_earnings_trend('AAPL')
        with open('tests/fixtures/yh-responses/earnings-trend.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_key_statistics(self):
        """ Test that a request successfully retrieves data if a
        valid key statistics request is made. """

        act_data = self.client.get_key_statistics('AAPL')
        with open('tests/fixtures/yh-responses/key-statistics.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_income_statement(self):
        """ Test that a request successfully retrieves data if a
        valid income statement request is made. """

        act_data = self.client.get_income_statement('AAPL')
        with open('tests/fixtures/yh-responses/income-statement.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_earnings(self):
        """ Test that a request successfully retrieves data if a
        valid earnings request is made. """

        act_data = self.client.get_earnings('AAPL')
        with open('tests/fixtures/yh-responses/earnings.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_net_share_purchase_activity(self):
        """ Test that a request successfully retrieves data if a
        valid net share purchase activity request is made. """

        act_data = self.client.get_net_share_purchase_activity('AAPL')
        with open('tests/fixtures/yh-responses/net-share-purchase-activity.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_upgrade_downgrade_history(self):
        """ Test that a request successfully retrieves data if a
        valid upgrade downgrade history request is made. """

        act_data = self.client.get_upgrade_downgrade_history('AAPL')
        with open('tests/fixtures/yh-responses/upgrade-downgrade-history.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_institution_ownership(self):
        """ Test that a request successfully retrieves data if a
        valid institution ownership request is made. """

        act_data = self.client.get_institution_ownership('AAPL')
        with open('tests/fixtures/yh-responses/institution-ownership.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_recommendation_trend(self):
        """ Test that a request successfully retrieves data if a
        valid recommendation trend request is made. """

        act_data = self.client.get_recommendation_trend('AAPL')
        with open('tests/fixtures/yh-responses/recommendation-trend.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)

    def test_get_balance_sheet(self):
        """ Test that a request successfully retrieves data if a
        valid balance_sheer request is made. """

        act_data = self.client.get_balance_sheet('AAPL')
        with open('tests/fixtures/yh-responses/balance-sheet.json', 'r') as f:
            exp_data = f.read()

        self.assertEqual(exp_data, act_data)