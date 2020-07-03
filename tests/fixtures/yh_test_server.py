import flask

ALLOWED_API_KEY = '0000000000'

app = flask.Flask(__name__)

def _get_response(filename):
    with open(filename, 'r') as f:
        return flask.Response(
            response=f.read(),
            status=200,
            mimetype='application/json'
        )

@app.route('/qu/quote/AAPL/earnings-history', methods = ['GET'])
def earnings_history():
    return _get_response('tests/fixtures/yh-responses/earnings-history.json')


@app.route('/qu/quote/AAPL/insider-holders', methods = ['GET'])
def insider_holders():
    return _get_response('tests/fixtures/yh-responses/insider-holders.json')

@app.route('/hi/history/AAPL/1d', methods = ['GET'])
def history():
    return _get_response('tests/fixtures/yh-responses/history.json')

@app.route('/qu/quote/AAPL/financial-data', methods = ['GET'])
def financial_data():
    return _get_response('tests/fixtures/yh-responses/financial-data.json')

@app.route('/qu/quote/AAPL/cashflow-statement', methods = ['GET'])
def cashflow_statement():
    return _get_response('tests/fixtures/yh-responses/cashflow-statement.json')

@app.route('/qu/quote/AAPL/insider-transactions', methods = ['GET'])
def insider_transactions():
    return _get_response('tests/fixtures/yh-responses/insider-transactions.json')

@app.route('/qu/quote/AAPL/asset-profile', methods = ['GET'])
def profile():
    return _get_response('tests/fixtures/yh-responses/profile.json')

@app.route('/qu/quote/AAPL/sec-filings', methods = ['GET'])
def sec_filings():
    return _get_response('tests/fixtures/yh-responses/sec-filings.json')

@app.route('/qu/quote/AAPL/calendar-events', methods = ['GET'])
def calendar_events():
    return _get_response('tests/fixtures/yh-responses/calendar-events.json')

@app.route('/qu/quote/AAPL/index-trend', methods = ['GET'])
def index_trend():
    return _get_response('tests/fixtures/yh-responses/index-trend.json')

@app.route('/qu/quote/AAPL/earnings-trend', methods = ['GET'])
def earnings_trend():
    return _get_response('tests/fixtures/yh-responses/earnings-trend.json')

@app.route('/qu/quote/AAPL/default-key-statistics', methods = ['GET'])
def key_statistics():
    return _get_response('tests/fixtures/yh-responses/key-statistics.json')

@app.route('/qu/quote/AAPL/income-statement', methods = ['GET'])
def income_statement():
    return _get_response('tests/fixtures/yh-responses/income-statement.json')

@app.route('/qu/quote/AAPL/earnings', methods = ['GET'])
def earnings():
    return _get_response('tests/fixtures/yh-responses/earnings.json')

@app.route('/qu/quote/AAPL/net-share-purchase-activity', methods = ['GET'])
def net_share_purchase_activity():
    return _get_response('tests/fixtures/yh-responses/net-share-purchase-activity.json')

@app.route('/qu/quote/AAPL/upgrade-downgrade-history', methods = ['GET'])
def upgrade_downgrade_history():
    return _get_response('tests/fixtures/yh-responses/upgrade-downgrade-history.json')

@app.route('/qu/quote/AAPL/institution-ownership', methods = ['GET'])
def institution_ownership():
    return _get_response('tests/fixtures/yh-responses/institution-ownership.json')

@app.route('/qu/quote/AAPL/recommendation-trend', methods = ['GET'])
def recommendation_trend():
    return _get_response('tests/fixtures/yh-responses/recommendation-trend.json')

@app.route('/qu/quote/AAPL/balance-sheet', methods = ['GET'])
def balance_sheet():
    return _get_response('tests/fixtures/yh-responses/balance-sheet.json')

@app.route('/mu/topmutualfunds', methods = ['GET'])
def mutual_funds():
    return _get_response('tests/fixtures/yh-responses/mutual-funds.json')

@app.route('/ga/topgainers', methods = ['GET'])
def top_gainers():
    return _get_response('tests/fixtures/yh-responses/top-gainers.json')

@app.route('/tr/trending', methods = ['GET'])
def most_watched():
    return _get_response('tests/fixtures/yh-responses/most-watched.json')

@app.route('/ne/news/AAPL', methods = ['GET'])
def news():
    return _get_response('tests/fixtures/yh-responses/news.json')

@app.route('/qu/quote/AAPL', methods = ['GET'])
def quote():
    return _get_response('tests/fixtures/yh-responses/quote.json')

@app.route('/et/topetfs', methods = ['GET'])
def etfs():
    return _get_response('tests/fixtures/yh-responses/etfs.json')

if __name__ == '__main__':
    app.run()