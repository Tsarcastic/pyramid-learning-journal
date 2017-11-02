"""Views for learning journal."""
from pyramid.response import Response
import io
import os
from pyramid.view import view_config
from entries import ENTRIES
HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/index.jinja2')
def list_view(request):
    """Display the list of entries."""
    return {'entries': ENTRIES}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Display a detail view of entry."""
    return {
        'title': 'a title',
        'creation_date': 'whatever',
        'body': 'my body'
        }


def create_view(request):
    """Display create a list entry."""
    path = os.path.join(HERE, '../templates/entry.html')
    with io.open(path) as res:
        return Response(res.read())


def update_view(request):
    """Display the update entry."""
    path = os.path.join(HERE, '../templates/edit.html')
    with io.open(path) as res:
        return Response(res.read())
