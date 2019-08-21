import requests
import quotes


def test_status_api():
    """test api returns with http 200"""
    response = requests.get(quotes.DEFAULT_URL.format('quotes'))
    assert response.status_code == 200

def test_return_correct_quote():
    """test return the correct quote"""
    obj = quotes.get_quote(1)
    print(obj)
    assert 'Explicit is better than implicit.' == obj

def test_return_quotes():
    """test return an obj with more than one quote"""
    obj = quotes.get_quotes()
    assert len(obj) > 0

def test_return_correct_quotes():
    """test return a quote"""
    obj = quotes.get_quotes()
    print(obj)
    assert 'Simple is better than complex.' in obj
