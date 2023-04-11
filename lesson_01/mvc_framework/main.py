def not_found(request):
    status = '404 NOT FOUND'
    body = 'NOT FOUND 404'
    return status, body


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts
        self.headers = [
            ('Content-Type', 'text/plain'),
        ]

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO')
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found

        request = {'environ': environ}
        for front in self.fronts:
            front(request)

        status, body = view(request)
        start_response(status, self.headers)
        return [body.encode('utf-8')]
