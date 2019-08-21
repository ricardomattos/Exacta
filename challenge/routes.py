
def includeme(config):
    """ include routes """
    # view
    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('quote', '/quote/{id}')
    config.add_route('random_quote', '/quotes/random')

    # api
    config.add_route('api_sessions', '/api/sessions')
    config.add_route('api_session', '/api/session/{id}')
