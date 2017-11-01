"""Views for learning journal."""
from pyramid.response import Response
import io
import os
from pyramid.view import view_config
HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/index.jinja2')
def list_view(request):
    """Display the list of entries."""
    return {}
    # path = os.path.join(HERE, '../templates/index.html')
    # with io.open(path) as res:
    #     return Response(res.read())


def detail_view(request):
    """Display a detail view of entry."""
    path = os.path.join(HERE, '../templates/detail.html')
    with io.open(path) as res:
        return Response(res.read())


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
