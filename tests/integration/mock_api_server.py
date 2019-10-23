import json

from flask import Flask, request, Response

ALLOWED_API_KEY = '0000000000'

app = Flask(__name__)

@app.route('/query', methods = ['GET'])
def query():
    api_key = request.args.get('apikey')
    function = request.args.get('function')
    symbol = request.args.get('symbol')
    interval = request.args.get('interval')
    output_size = request.args.get('outputsize')
    data_type = request.args.get('datatype')

    if output_size is None :
        output_size = 'compact'
    if data_type is None :
        data_type = 'json'

    if api_key is None or api_key != ALLOWED_API_KEY:
        return Response(
            response='forbidden', 
            status=401, 
            mimetype='text/plain'
        )

    if function == 'TIME_SERIES_INTRADAY':
        if symbol is not None and interval is not None:
            return Response(
                response=json.dumps(request.args), 
                status=200, 
                mimetype='application/json'
            )            
        else:
            return Response(
                response='invalid parameters', 
                status='400', 
                mimetype='text/plain'
            )
         
    elif function in ['TIME_SERIES_DAILY','TIME_SERIES_DAILY_ADJUSTED']:
        if symbol is not None:
            return Response(
                response=json.dumps(request.args), 
                status=200, 
                mimetype='application/json'
            )
    else:
        return Response(
            response='not found', 
            status=404, 
            mimetype='text/plain'
        )

if __name__ == '__main__':
    app.run()