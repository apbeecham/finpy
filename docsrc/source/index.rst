finpy-0.3.0
=================================

About
#####
Finpy is a collection of api clients that aims to provide a centralised source of mechanical and fundamental
financial data from a range of providers.

Contents
########
.. toctree::
   :maxdepth: 1

Quickstart
##########
Get up and running in three easy steps:

1. Import your favourite api wrapper:

.. code-block:: python

    from finpy import alphavantage as av

2. Create a client:

.. code-block:: python

    client = av.StockClient(my_api_key)

3. Request data:

.. code-block:: python

    client.get_daily_data('MSFT')

API's
#####
Supported apis are listed below. You will need to register with these providers in order to retrieve an api key
for use with our api clients.

* (partial) `alphavantage <https://www.alphavantage.co>`_
* (partial) `yahoo <https://rapidapi.com/apidatacenter-api-data/api/yahoo-finance15>`_

Indices and tables
##################
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
