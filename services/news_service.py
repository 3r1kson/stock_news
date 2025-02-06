import requests

from config.config import get_news_key


def get_news(date):
    key = get_news_key()

    url = f'https://newsapi.org/v2/everything?q=tesla&from={date}&sortBy=publishedAt&apiKey={key}'
    r = requests.get(url)
    return r.json()