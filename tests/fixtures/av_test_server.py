import json

import flask

ALLOWED_API_KEY = '0000000000'

app = flask.Flask(__name__)

@app.route('/query', methods = ['GET'])
def query():
    api_key = flask.request.args.get('apikey')
    function = flask.request.args.get('function')
    symbol = flask.request.args.get('symbol')
    interval = flask.request.args.get('interval')
    output_size = flask.request.args.get('outputsize')
    data_type = flask.request.args.get('datatype')

    if output_size is None :
        output_size = 'compact'
    if data_type is None :
        data_type = 'json'

    if api_key is None or api_key != ALLOWED_API_KEY:
        return flask.Response(
            response='forbidden',
            status=401,
            mimetype='text/plain'
        )

    if function == 'TIME_SERIES_INTRADAY':
        if symbol is not None and interval is not None:
            return flask.Response(
                response=json.dumps(flask.request.args),
                status=200,
                mimetype='application/json'
            )
        else:
            return flask.Response(
                response='invalid parameters',
                status='400',
                mimetype='text/plain'
            )

    elif function in ['TIME_SERIES_DAILY','TIME_SERIES_DAILY_ADJUSTED']:
        if symbol is not None:
            return flask.Response(
                response=json.dumps(flask.request.args),
                status=200,
                mimetype='application/json'
            )
    else:
        return flask.Response(
            response='not found',
            status=404,
            mimetype='text/plain'
        )

if __name__ == '__main__':
    app.run()