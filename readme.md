![ci](https://github.com/apbeecham/finpy/workflows/ci/badge.svg)

finpy
===

Python wrappers for financial data apis.

## Quickstart

1. Import your favourite api wrapper
    ```python
    from finpy.alphavantage import api
    ```
2. Create an api object
    ```python
    stock_api = api.StockApi(my_api_key)
    ```
3. Request data
    ```python
    stock_api.get_daily_data('MSFT')
    ```

## Wrappers
We support the following apis:

- [alphavantage](https://www.alphavantage.co)
