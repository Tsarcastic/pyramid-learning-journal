
from datetime import datetime
from pyramid_learning_journal.models import MyModel
from pyramid_learning_journal.views.default import (
    list_view,
    detail_view,
    update_view,
    create_view
    )


def test_home_route_get_request_200_ok(testapp):
    """."""
    response = testapp.get('/')
    assert response.status_code == 200


def test_home_with_no_entries(testapp):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find('div')
    assert 'article' not in content


def test_create_view_post_empty_is_empty_dict(dummy_request):
    """POST requests without data should return an empty dictionary."""
    dummy_request.method = "POST"
    response = create_view(dummy_request)
    assert response == {}


def test_home_with_one_entry(testapp, fill_my_db):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('article')
    assert len(content) == 1


def test_home_with_many_entries(testapp, more_db):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('article')
    assert len(content) == 4


def test_add_new_entry_200(testapp, dummy_request):
    """."""
    dummy_request.method = testapp.get('/journal/new-entry')
    assert dummy_request.response.status == '200 OK'


def test_add_new_entry_something(testapp, dummy_request):
    """."""
    dummy_request.method = testapp.get('/journal/new-entry')
    entry = MyModel(
        title='Test Title',
        body='This is a test body of text.',
        creation_date=datetime.now()
        )


def test_create_view_returns_title(dummy_request):
    """Update view response has file content."""
    from pyramid_learning_journal.views.default import create_view
    request = dummy_request
    response = create_view(request)
    assert response == {}
