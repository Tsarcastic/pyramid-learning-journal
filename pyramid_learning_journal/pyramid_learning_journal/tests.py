import unittest
import transaction
import pytest
from pyramid import testing
from pyramid_learning_journal.models import MyModel, get_tm_session
from pyramid_learning_journal.models.meta import Base
from pyramid_learning_journal.views.default import (
    list_view,
    detail_view,
    update_view,
    create_view
    )

import random
import datetime


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



# import faker
# def test_list_view_returns_200():

ENTRIES = [
    {
        'title': "Day 13",
        'text': "### Today I learned: - Implement priority queue - SQLAlchemy (avoid sql injection security risk) - object relational mapper (translation layer your code --> SQL) - models/mymodels.py -- import models in models/__init__ - in model import Unicode Float DateTime - add correct Columns - set create date.now() in __init__ for model class - add and commit to get it in your db - many query methods - initializedb.py ---line 38:--- Base.metadata.drop_all(engine) - initdb development.ini - set in ENV/bin/activate export DATABASE_URL=' postgres://localhost:5432/learning_journal' - os.eviron[DATABASE_URL] - remove from development.ini and production - update __init__.py settings['sqlalchemy.url'] = os.eviron[DATABASE_URL] - then initializedb.py same line",
        'author': {
            'course_id': [
                "sea401d7"
                ],
            'username': "ChristopherSClosser",
            'id': 45,
            'display_name': "ChristopherSClosser"
        },
        'id': 893,
        'markdown': "<h3>Today I learned:</h3> <ul> <li>Implement priority queue</li> <li>SQLAlchemy (avoid sql injection security risk)<ul> <li>object relational mapper (translation layer your code --&gt; SQL)</li> </ul> </li> <li>models/mymodels.py -- import models in models/<strong>init</strong></li> <li>in model import Unicode Float DateTime<ul> <li>add correct Columns</li> <li>set create date.now() in <strong>init</strong> for model class</li> </ul> </li> <li>add and commit to get it in your db</li> <li>many query methods</li> <li>initializedb.py ---line 38:--- Base.metadata.drop_all(engine)<ul> <li>initdb development.ini</li> </ul> </li> <li>set in ENV/bin/activate export DATABASE_URL=' postgres://localhost:5432/learning_journal'</li> <li>os.eviron[DATABASE_URL]</li> <li>remove from development.ini and production</li> <li>update <strong>init</strong>.py settings['sqlalchemy.url'] = os.eviron[DATABASE_URL]<ul> <li>then initializedb.py same line</li> </ul> </li> </ul>",
        'created': "2017-11-02T01:20:34.210642"
    },
    {
        'title': "Day 12",
        'text': "### Today I learned - Binary heap min and max - Start to Implement max heap - Using jinja2 templates - MVC - Pyramid Renderers - Group project selection",

        'id': 888,
        'markdown': "<h3>Today I learned</h3> <ul> <li>Binary heap min and max<ul> <li>Start to Implement max heap</li> </ul> </li> <li>Using jinja2 templates</li> <li>MVC</li> <li>Pyramid Renderers</li> <li>Group project selection</li> </ul>",
        'created': "2017-11-01T15:33:24.823650"
    }]


@pytest.fixture
def dummy_request():
    """Instantiate a fake HTTP Request, complete with a database session.
    This is a function-level fixture, so every new request will have a
    new database session.
    """
    return {'entries': ENTRIES}


def test_list_view_returns_objects(dummy_request):
    """Test that the list view does return objects when the entries is populated.
    """
    result = list_view(dummy_request)
    for item in result['entries']:
        print(item)
    assert len(result["entries"]) == 13
