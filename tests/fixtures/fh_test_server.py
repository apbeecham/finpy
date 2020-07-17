import json
import flask

app = flask.Flask(__name__).m

def _get_response(filename):
    with open(filename, 'r') as f:
        return flask.Response(
            response=f.read(),
            status=200,
            mimetype='application/json'
        )

@app.route('/stock/profile2', methods = ['GET'])
def profile():
    symbol = flask.request.args.get('symbol')

    if symbol == 'AAPL':
        return _get_response('tests/fixtures/fh-responses/profile.json')
    else:
        return flask.Response(status=404)

@app.route('/stock/symbols', methods = ['GET'])
def symbols():
    exchange = flask.request.args.get('exchange')

    if exchange == 'LSE':
        return _get_response('tests/fixtures/fh-responses/symbols.json')
    else:
        return flask.Response(status=404)

@app.route('/news', methods = ['GET'])
def market_news():
    category = flask.request.args.get('category')

    if category == 'general':
        return _get_response('tests/fixtures/fh-responses/market-news.json')
    else:
        return flask.Response(status=404)

@app.route('/company-news', methods = ['GET'])
def news():
    symbol = flask.request.args.get('symbol')
    start = flask.request.args.get('from')
    end = flask.request.args.get('to')

    if symbol == 'AAPL':
        return _get_response('tests/fixtures/fh-responses/news.json')
    else:
        return flask.Response(status=404)

@app.route('/news-sentiment', methods = ['GET'])
def news_sentiment():
    symbol = flask.request.args.get('symbol')

    if symbol == 'AAPL':
        return _get_response('tests/fixtures/fh-responses/news-sentiment.json')
    else:
        return flask.Response(status=404)

@app.route('/stock/peers', methods = ['GET'])
def peers():
    symbol = flask.request.args.get('symbol')

    if symbol == 'AAPL':
        return _get_response('tests/fixtures/fh-responses/peers.json')
    else:
        return flask.Response(status=404)

@app.route('/stock/metric', methods = ['GET'])
def basic_financials():
    symbol = flask.request.args.get('symbol')
    metric = flask.request.args.get('metric')

    if symbol == 'AAPL' and metric == 'all':
        return _get_response('tests/fixtures/fh-responses/basic-financials.json')
    else:
        return flask.Response(status=404)

@app.route('/financials-reported', methods = ['GET'])
def financials_as_reported():
    symbol = flask.request.args.get('symbol')

    if symbol == 'AAPL':
        return _get_response('tests/fixtures/fh-responses/financials-reported.json')
    else:
        return flask.Response(status=404)

@app.route('/stock/filings', methods = ['GET'])
def filings():
    symbol = flask.request.args.get('symbol')

    if symbol == 'AAPL':
        return _get_response('tests/fixtures/fh-responses/filings.json')
    else:
        return flask.Response(status=404)

@app.route('/calendar/ipo', methods = ['GET'])
def ipo_calendar():
    start = flask.request.args.get('from')
    end = flask.request.args.get('to')

    if start and end:
        return _get_response('tests/fixtures/fh-responses/ipo-calendar.json')
    else:
        return flask.Response(status=404)