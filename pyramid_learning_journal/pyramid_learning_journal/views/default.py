"""Views for learning journal."""
from pyramid.response import Response
import io
import os
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from entries import ENTRIES
from ..models import MyModel
import datetime

import pdb
HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/index.jinja2')
def list_view(request):
    """Display the list of entries."""
    query = request.dbsession.query(MyModel)
    entries = query.order_by(MyModel.creation_date.desc()).all()
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
    if request.POST:
        entry = MyModel(
            title=request.POST["title"],
            creation_date=datetime.datetime.now(),
            body=request.POST["body"]
        )
        request.dbsession.add(entry)
        return HTTPFound(request.route_url('home'))
    return {}


@view_config(route_name='edit', renderer='../templates/editEntry.jinja2')
def update_view(request):
    """Display the update entry."""
    ident = int(request.matchdict["id"])
    entry = request.dbsession.query(MyModel).get(ident)
    if request.POST:
        entry.title = request.POST["title"]
        entry.body = request.POST["body"]
        request.dbsession.flush()
        return HTTPFound(request.route_url('home'))

    form_fill = {
        "title": entry.title,
        "body": entry.body
    }
    return {"entry": form_fill}
