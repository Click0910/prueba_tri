import requests
import functools


stocks_list = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'TWTR', 'UBER', 'LYFT', 'SNAP', 'SHOP']
URL = 'https://financialmodelingprep.com/api/v3/quote-short/'

API_KEY = 'c13a5d2ecf7cc6b8c50c06d7e1dfce22'

params = {
    'apikey': API_KEY
}


@functools.cache
def find_total_price():

    total_price = 0

    for stock in stocks_list:
        response = requests.get(URL+stock, params=params).json()
        price = response[0]['price']
        total_price += price

    print(total_price)


def user_porfolio():

    pass
    # Missing context, with the info gotten in the assessment is not enough to start to develop this task.
    # More info is required.



