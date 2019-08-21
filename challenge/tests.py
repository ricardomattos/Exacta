import unittest
import transaction
from pyramid import testing


def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        from .models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from .models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from .models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)


class TestViewsSuccessCondition(BaseTest):

    def setUp(self):
        super(TestViewsSuccessCondition, self).setUp()
        self.init_database()

        from .models.session import Session

        model = Session(
            session_id='abc123',
            page='/page',
            date='2019-08-21 17:18:16.442005',
        )
        self.session.add(model)

    def test_return_home_view(self):
        from .views import home
        res = home(dummy_request(self.session))
        self.assertIn('msg', res)
        self.assertEqual(res['msg'], 'Desafio Web 1.0')
    
    def test_return_quote_view(self):
        from .views import quote
        req = dummy_request(self.session)
        req.matchdict['id'] = 1
        res = quote(req)
        self.assertIn('quote', res)
        self.assertEqual(res['quote'], 'Explicit is better than implicit.')

    def test_return_quotes_view(self):
        from .views import quotes
        res = quotes(dummy_request(self.session))
        self.assertIn('quotes', res)
        self.assertTrue(len(res['quotes']) > 0)
