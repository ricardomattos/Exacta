import json
from pyramid.view import view_defaults, view_config
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import class_mapper
from .models import Session


def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    # get the names of all the columns on model
    columns = [c.key for c in class_mapper(model.__class__).columns]
    # then return their values in a dict
    return dict((c, str(getattr(model, c))) for c in columns)


@view_defaults(renderer='templates/api.pt')
class APIlViews():
    """Class with api views"""

    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', route_name='api_sessions')
    def sessions(self):
        """View to get all Sessions saved"""
        try:
            sessions = [serialize(s) for s in self.request.dbsession.query(Session).all()]
        except DBAPIError as db_err_msg:
            return Response(db_err_msg, content_type='text/plain', status=500)
        return Response(json.dumps(sessions).encode('UTF-8'), content_type="application/json")

    @view_config(request_method='GET', route_name='api_session')
    def session(self):
        """View to get Session info by id"""
        try:
            idx = self.request.matchdict['id']
            session = serialize(self.request.dbsession.query(Session).filter_by(uid=idx).first())
        except DBAPIError as db_err_msg:
            return Response(db_err_msg, content_type='text/plain', status=500)
        return Response(json.dumps(session).encode('UTF-8'), content_type="application/json")

