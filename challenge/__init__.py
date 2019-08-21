from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config


session_factory = SignedCookieSessionFactory('itsaseekreet')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.set_session_factory(session_factory)
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
