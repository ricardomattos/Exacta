import random
import logging
from uuid import uuid4
from datetime import datetime
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from quotes import get_quotes, get_quote
from . import models


log = logging.getLogger(__name__)

def manage_sessions(func):
    """Manage Session for each request"""

    def wrapper(context, request):
        """Register Session info in the database"""
        response = func(context, request)
        log.info('session new? - %s', request.session.new)

        if request.session.new:
            request.session['session_id'] = uuid4().hex
        request.session['page'] = request.path[1:]
        request.session['date'] = datetime.now()

        try:
            request.dbsession.add(models.Session(
                session_id=request.session['session_id'],
                page=request.session['page'],
                date=request.session['date'],
            ))
        except DBAPIError as db_err_msg:
            return Response(db_err_msg, content_type='text/plain', status=500)

        return response
    return wrapper

@view_config(request_method='GET', route_name='home', renderer='templates/home.pt', decorator=(manage_sessions))
def home(request):
    """Home View"""
    return {'msg': 'Desafio Web 1.0'}

@view_config(request_method='GET', route_name='quotes', renderer='templates/quotes.pt', decorator=(manage_sessions))
def quotes(request):
    """Quotes View to get all get quotes"""
    quotes_ = get_quotes()
    return {'quotes': quotes_}

@view_config(request_method='GET', route_name='quote', renderer='templates/quote.pt', decorator=(manage_sessions))
def quote(request):
    """Quote View to get a single quote by id"""
    idx = request.matchdict['id']
    quote_ = get_quote(idx)
    return {'quote': quote_}

@view_config(request_method='GET', route_name='random_quote', renderer='templates/random.pt', decorator=(manage_sessions))
def random_quote(request):
    """Random Quote View to get a random quote"""
    quotes_ = get_quotes()
    index = random.randrange(len(quotes_))
    return {'index': index, 'quote': quotes_[index]}
 