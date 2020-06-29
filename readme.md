![build](https://github.com/apbeecham/finpy/workflows/build/badge.svg)
![docs](https://github.com/apbeecham/finpy/workflows/docs/badge.svg)

finpy
===

Python wrappers for financial data apis.

## Quickstart

1. Import your favourite api wrapper
.. code-block:: python
   from finpy.alphavantage import api

2. Create an api object
.. code-block:: python
   stock_api = api.StockApi(my_api_key)

3. Request data
.. code-block:: python
   stock_api.get_daily_data('MSFT')


## Wrappers
We support the following apis:

- [alphavantage](https://www.alphavantage.co)
