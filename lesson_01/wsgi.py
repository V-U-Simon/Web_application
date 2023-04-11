from pprint import pprint
import sys
import subprocess


def index():
    status = '200 OK'
    body = 'index'.encode('utf-8')
    return status, body


def info():
    status = '200 OK'
    body = 'info'.encode('utf-8')
    return status, body


def not_found():
    status = '404 NOT FOUND'
    body = 'NOT FOUND 404'.encode('utf-8')
    return status, body


routes = {
    '/': index,
    '/info': info,
}


class Application:

    def __init__(self, routes):
        self.routes = routes
        self.headers = [('Content-Type', 'text/plain')]

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO')
        if path in self.routes:
            status, body = self.routes[path]()
            start_response(status, self.headers)
            return [body]
        else:
            status, body = not_found()
            start_response(status, self.headers)
            return [body]


application = Application(routes)

if __name__ == '__main__':
    process_res = subprocess.run(
        [f'uwsgi', '--socket', ':8080', '--protocol=http', '--wsgi-file', f'{__file__}', '--callable', 'application'],
        stdout=sys.stdout,
        stderr=sys.stdout,
        text=True,
    )
