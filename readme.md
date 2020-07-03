![build](https://github.com/apbeecham/finpy/workflows/build/badge.svg)
![docs](https://github.com/apbeecham/finpy/workflows/docs/badge.svg)

finpy-0.3.0
===

## About
Finpy is a collection of api clients that aims to provide a centralised source of mechanical and fundamental
financial data from a range of providers.

## Quickstart
1. Import your favourite api
    ```python
   from finpy import alphavantage as av
    ```
2. Create an api client
    ```python
   client = av.StockClient(my_api_key)
    ```
3. Request data
    ```python
   data = client.get_daily_data('MSFT')
    ```

## API's
Supported apis are listed below. You will need to register with these providers in order to retrieve an api key
for use with our api clients.

- (partial)[alphavantage](https://www.alphavantage.co)
- (partial)[yahoo](https://rapidapi.com/apidatacenter-api-data/api/yahoo-finance15)

## Documentation
View the latest documentation [here](https://apbeecham.github.io/finpy/).
