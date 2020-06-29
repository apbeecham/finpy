finpy
=================================
financial data apis for python.

Contents
########

.. toctree::
   :maxdepth: 1

Quickstart
##########
Get up and running in three easy steps:

1. Import your favourite api wrapper:

.. code-block:: python

    from finpy.alphavantage import api

2. Create an api object*:

.. code-block:: python

    stock_api = api.StockApi(my_api_key)

3. Request data:

.. code-block:: python

    stock_api.get_daily_data('MSFT')

\*api keys not included.


Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
