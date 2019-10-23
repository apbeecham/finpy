# fail immediately on error
set -e

# score code
pip install pylint-fail-under
pip install ./
pylint-fail-under --fail_under 9.0 ./alphavantage/api.py