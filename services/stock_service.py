import requests

from config.config import get_stock_key


def get_stock(stock):
    key = get_stock_key()
    print(key)
    function = "TIME_SERIES_DAILY"

    url = f'https://www.alphavantage.co/query?function={function}&symbol={stock}&apikey={key}'
    r = requests.get(url)
    return r.json()
