from setuptools import setup
setup(
    name='finpy',
    version='0.3.0',
    description='python clients for financial data apis.',
    author='Adam Beecham',
    author_email='apbeecham91@gmail.com',
    packages=['finpy'],
    install_requires=['requests']
)