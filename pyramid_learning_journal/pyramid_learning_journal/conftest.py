"""Test fixtures and setup and teardown."""
from pyramid.config import Configurator
from pyramid_learning_journal.models.meta import Base
from pyramid_learning_journal.models import MyModel
from pyramid import testing
import pytest
from datetime import datetime

import os


def main(global_config, **settings):
    """."""
    settings["sqlalchemy.url"] = os.environ["TESTDB"]
    config = Configurator(settings=settings)
    config.add_static_view(name='static',
                           path='pyramid_learning_journal:static')
    config.include('pyramid_jinja2')
    config.include('pyramid_learning_journal.routes')
    config.include('pyramid_learning_journal.models')
    config.scan()
    return config.make_wsgi_app()


@pytest.fixture
def testapp(request):
    """Fixture for a fully-configured test application."""
    from webtest import TestApp
    app = main({})

    SessionFactory = app.registry['dbsession_factory']
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)
    return TestApp(app)


@pytest.fixture
def fill_my_db(testapp):
    """."""
    SessionFactory = testapp.app.registry['dbsession_factory']
    session = SessionFactory()
    test_entry = MyModel(
        title='Test Title',
        body='This is a test body of text.',
        creation_date=datetime.now()
    )
    session.add(test_entry)
    session.commit()


@pytest.fixture
def more_db(testapp):
    """."""
    SessionFactory = testapp.app.registry['dbsession_factory']
    session = SessionFactory()
    res = []
    test_entries = [{
            'title': 'Test Title One',
            'body': 'This is a test body of text.',
            'creation_date': datetime.now()
            },
        {
            'title': 'Test Title Two',
            'body': 'This is a test body of text.',
            'creation_date': datetime.now()
            },
        {
            'title': 'Test Title Three',
            'body': 'This is a test body of text.',
            'creation_date': datetime.now()
            },
        {
            'title': 'Test Title Four',
            'body': 'This is a test body of text.',
            'creation_date': datetime.now()
    }]
    for entry in test_entries:
        # import pdb; pdb.set_trace()
        res.append(MyModel(title=entry['title'],
                           body=entry['body'],
                           creation_date=datetime.now()))

    session.add_all(res)
    session.commit()


@pytest.fixture
def dummy_request(testapp):
    """Instantiate a fake HTTP Request.

    complete with a database session.
    This is a function-level fixture, so every new request will have a
    new database session.
    """
    return testing.DummyRequest(dbsession=testapp)
