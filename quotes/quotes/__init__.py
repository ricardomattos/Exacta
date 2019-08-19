import json
import random
import requests


DEFAULT_URL = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/{}/'


def unserialize(content):
    """Unserialize objects"""
    return json.loads(content)


def make_request(url):
    """Make request to api"""
    resp = requests.get(url)
    content = resp.content.decode('utf-8')
    return unserialize(content)


def get_quotes():
    """Get all quotes from api"""
    url = DEFAULT_URL.format('quotes')
    resp = make_request(url)
    return resp['quotes']


def get_quote(quote_number):
    """Get one quote from api"""
    url = DEFAULT_URL.format('quotes') + str(quote_number)
    resp = make_request(url)
    return resp['quote']
