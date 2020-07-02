import enum
import requests

class Interval(enum.Enum):
    """ Possible interval values for history requests. """

    M5 = '5m'
    M15 = '15m'
    M30 = '30m'
    HOUR = '1h'
    DAY = '1d'
    WEEK = '1wk'
    MONTH = '1m'
    QTR = '3m'

    def __str__(self):
        return self.value

class Client:
    """ A client for the yahoo stocks api. Provides historic
    price and fundamental data for equities.

    Args:
        api_key (str): A yahoo api key.
    """
    API_URL = 'https://yahoo-finance15.p.rapidapi.com/api/yahoo/'

    def __init__(self, api_key):
        self._session = requests.Session()

        self._session.headers = {
            'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
            'x-rapidapi-key': api_key
        }

    def get_earnings_history(self, symbol):
        """ Request earnings history information for the provided
        symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing earnings history for
                the provided symbol.
        """
        end_point = 'qu/quote/{}/earnings-history'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_insider_holders(self, symbol):
        """ Request  insider holders' information for the provided
        symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing insider holders' information
                for the provided symbol.
        """
        end_point = 'qu/quote/{}/insider-holders'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_history(self, symbol, interval='1d'):
        """ Request historic data for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing historic data
                for the provided symbol.
        """
        end_point = 'hi/history/{}/{}'.format(symbol, Interval(interval))
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_financial_data(self, symbol):
        """ Request financial data for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing financial data for the
                provided symbol.
        """
        end_point = 'qu/quote/{}/financial-data'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_cashflow_statement(self, symbol):
        """ Request cashflow statements for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing cashflow statements for the
                provided symbol.
        """
        end_point = 'qu/quote/{}/cashflow-statement'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_insider_transactions(self, symbol):
        """ Request insider transactions for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing insider transactions for the
                provided symbol.
        """
        end_point = 'qu/quote/{}/insider-transactions'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_profile(self, symbol):
        """ Request profile information for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing profile information for the
                provided symbol.
        """
        end_point = 'qu/quote/{}/asset-profile'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_sec_filings(self, symbol):
        """ Request sec filings for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing sec filings for the
                provided symbol.
        """
        end_point = 'qu/quote/{}/sec-filings'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_calendar_events(self, symbol):
        """ Request calendar events for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing calendar events for the
                provided symbol.
        """
        end_point = 'qu/quote/{}/calendar-events'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_index_trend(self, symbol):
        """ Request index trend earnings history information for the
        provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing index trend earnings history
                information for the provided symbol.
        """
        end_point = 'qu/quote/{}/index-trend'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_earnings_trend(self, symbol):
        """ Request earnings trend history information for the
        provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing earnings trend history
                information for the provided symbol.
        """
        end_point = 'qu/quote/{}/earnings-trend'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_key_statistics(self, symbol):
        """ Request key statistics data for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing key statistics for the provided symbol.
        """
        end_point = 'qu/quote/{}/default-key-statistics'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_income_statement(self, symbol):
        """ Request income statement data for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing income statement data
                information for the provided symbol.
        """
        end_point = 'qu/quote/{}/income-statement'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_earnings(self, symbol):
        """ Request earnings information for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing earnings information
                for the provided symbol.
        """
        end_point = 'qu/quote/{}/earnings'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_net_share_purchase_activity(self, symbol):
        """ Request net share purchase activity information for the
        provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing net share purchase activity
                information for the provided symbol.
        """
        end_point = 'qu/quote/{}/net-share-purchase-activity'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_upgrade_downgrade_history(self, symbol):
        """ Request upgrade downgrade history for the
        provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing upgrade downgrade
                history for the provided symbol.
        """
        end_point = 'qu/quote/{}/upgrade-downgrade-history'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_institution_ownership(self, symbol):
        """ Request institution ownership data for the
        provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing institution ownership data
                for the provided symbol.
        """
        end_point = 'qu/quote/{}/institution-ownership'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_recommendation_trend(self, symbol):
        """ Request recommendation and trend data for the
        provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing recommendation and trend data
                for the provided symbol.
        """
        end_point = 'qu/quote/{}/recommendation-trend'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text

    def get_balance_sheet(self, symbol):
        """ Request balance sheet data for the provided symbol.

        Args:
            symbol (str): The symbol for the target stock (e.g. AAPL).

        Returns:
            str: A json string containing balance sheet data
                for the provided symbol.
        """
        end_point = 'qu/quote/{}/balance-sheet'.format(symbol)
        response = self._session.get(self.API_URL + end_point)
        return response.text
