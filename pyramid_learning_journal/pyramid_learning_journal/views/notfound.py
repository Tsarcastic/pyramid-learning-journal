from pyramid.view import notfound_view_config


@notfound_view_config(route_name='not-found', renderer='../templates/404.jinja2')
def notfound_view(request):
    # request.response.status = 404
    return {'not-found': request.response.renderer}
