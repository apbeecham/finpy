from setuptools import setup
setup(
    name='finpy',
    version='0.1.0',
    description='Wrappers for financial data apis.',
    author='Adam Beecham',
    author_email='apbeecham91@gmail.com',
    packages=['alphavantage'],
    install_requires=['requests']
)