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


def application(environ, start_response):
    global routes
    headers = [('Content-Type', 'text/plain')]

    path = environ.get('PATH_INFO')
    if path in routes:
        status, body = routes[path]()
        start_response(status, headers)
        return [body]
    else:
        status, body = not_found()
        start_response(status, headers)
        return [body]


if __name__ == '__main__':
    process_res = subprocess.run(
        [f'uwsgi', '--socket', ':8080', '--protocol=http', '--wsgi-file', f'{__file__}', '--callable', 'application'],
        stdout=sys.stdout,
        stderr=sys.stdout,
        text=True,
    )
