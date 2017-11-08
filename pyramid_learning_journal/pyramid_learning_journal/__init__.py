"""."""
from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
    config = Configurator(settings=settings)
    config.add_static_view(name='static', path='pyramid_learning_journal:static')
    config.include('.views')
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
