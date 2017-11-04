"""Views for learning journal."""
from pyramid.response import Response
import io
import os
from pyramid.view import view_config
from entries import ENTRIES
from ..models import MyModel

import pdb
HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/index.jinja2')
def list_view(request):
    """Display the list of entries."""
    entries = request.dbsession.query(MyModel).all()
    return {'entries': entries}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Display a detail view of entry."""
    ident = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(ident)
    if not entry:
        return Response('not-found', status=404)
    return {"entry": entry}


@view_config(route_name='new', renderer='../templates/newEntry.jinja2')
def create_view(request):
    """Display create a list entry."""
    return {}


def update_view(request):
    """Display the update entry."""
    path = os.path.join(HERE, '../templates/edit.html')
    with io.open(path) as res:
        return Response(res.read())
