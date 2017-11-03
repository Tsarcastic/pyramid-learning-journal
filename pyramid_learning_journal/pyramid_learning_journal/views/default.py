"""Views for learning journal."""
from pyramid.response import Response
import io
import os
from pyramid.view import view_config
from entries import ENTRIES
import pdb
HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/index.jinja2')
def list_view(request):
    """Display the list of entries."""
    return {'entries': ENTRIES}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Display a detail view of entry."""
    ident = int(request.matchdict['id'])
    for entry in ENTRIES:
        if int(entry['id']) == ident:  # if entry.id is str
            return {'entry': entry}


@view_config(route_name='new', renderer='../templates/newEntry.jinja2')
def create_view(request):
    """Display create a list entry."""
    return {}


def update_view(request):
    """Display the update entry."""
    path = os.path.join(HERE, '../templates/edit.html')
    with io.open(path) as res:
        return Response(res.read())
