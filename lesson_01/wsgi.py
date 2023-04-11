from pprint import pprint
import sys
import subprocess
from lesson_01.templator import render


def index(request):
    status = '200 OK'
    body = 'index'
    return status, render('lesson_01/stub.html', request)


class Info:

    def __call__(self, request):
        status = '200 OK'
        body = 'info'.encode('utf-8')
        return status, body


def not_found(request):
    status = '404 NOT FOUND'
    body = 'NOT FOUND 404'
    return status, body


routes: dict[str, callable] = {
    '/': index,
    '/info': Info(),
}


def fill_request(request: dict):
    request['key'] = 'value'


def fill_request_2(request: dict):
    request['other_key'] = 'other_value'


fronts = [fill_request, fill_request_2]


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


application = Application(routes, fronts)

if __name__ == '__main__':
    process_res = subprocess.run(
        [f'uwsgi', '--socket', ':8080', '--protocol=http', '--wsgi-file', f'{__file__}', '--callable', 'application'],
        stdout=sys.stdout,
        stderr=sys.stdout,
        text=True,
    )
