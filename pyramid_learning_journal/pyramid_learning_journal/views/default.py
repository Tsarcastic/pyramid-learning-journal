"""Views for learning journal."""
from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """Display the list of entries."""
    res = os.open(os.path.join(HERE, '/data/index.html')).read()
    os.close()
    return Response(res)


def detail_view():
    """Display a detail view of entry."""
    pass


def create_view():
    """Display create a list entry."""
    pass


def update_view():
    """Display the update entry."""
    pass
