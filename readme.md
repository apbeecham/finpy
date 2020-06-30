![build](https://github.com/apbeecham/finpy/workflows/build/badge.svg)
![docs](https://github.com/apbeecham/finpy/workflows/docs/badge.svg)

finpy
===

Finpy is a collection of finance api clients providing a centralised source of mechanical and fundamental
financial data.

## Quickstart

1. Import your favourite api
    ```python
   from finpy import alphavantage as av
    ```
2. Create an api client
    ```python
   client = av.stocks.Client(my_api_key)
    ```
3. Request data
    ```python
   data = client.get_daily_data('MSFT')
    ```

## API's
We support the below apis hosted on rapidapi. We do not provide api keys, you will need to subscribe to your preferred apis before using the provided finpy clients.

- [alphavantage](https://rapidapi.com/alphavantage/api/alpha-vantage)
- [yahoo](https://rapidapi.com/apidatacenter-api-data/api/yahoo-finance15)

## Documentation
Full documentation links:
- [0.1.0](https://apbeecham.github.io/finpy/)
