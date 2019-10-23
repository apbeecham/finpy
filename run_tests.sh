#!/bin/bash

# fail immediately on error
set -e

# install and start test server
pip install flask
python ./tests/integration/mock_api_server.py &

# install required libs
pip install ./
python -m unittest