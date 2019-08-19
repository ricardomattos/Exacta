import unittest
import requests
import quotes


class APITest(unittest.TestCase):
    """API test"""

    def test_status_api(self):
        """test api returns with http 200"""
        response = requests.get(quotes.DEFAULT_URL.format('quotes'))
        self.assertEqual(response.status_code, 200)


class GetQuoteTest(unittest.TestCase):
    """get_quote tests"""

    def test_return_correct_quote(self):
        """test return the correct quote"""
        obj = quotes.get_quote(1)
        self.assertIn('Explicit is better than implicit', obj)


class GetQuotesTest(unittest.TestCase):
    """get_quotes tests"""

    def test_return_quotes(self):
        """test return an obj with more than one quote"""
        obj = quotes.get_quotes()
        self.assertTrue(len(obj) > 0)

    def test_return_correct_quote(self):
        """test return the correct quote"""
        obj = quotes.get_quotes()
        self.assertIn('Explicit is better than implicit.', obj)
