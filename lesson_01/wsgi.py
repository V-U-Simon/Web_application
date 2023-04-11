from pprint import pprint
import sys
import subprocess


def application(environ, start_response):
    pprint(environ)

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
    ]

    if environ.get('PATH_INFO') == '/':
        body = 'index'.encode('utf-8')
        start_response(status, headers)
        return [body]
    elif environ.get('PATH_INFO') == '/info':
        body = 'info'.encode('utf-8')
        start_response(status, headers)
        return [body]
    else:
        body = 'NOT FOUND 404'.encode('utf-8')
        status = '404 NOT FOUND'
        start_response(status, headers)
        return [body]


if __name__ == '__main__':

    process_res = subprocess.run(
        [f'uwsgi', '--socket', ':8080', '--protocol=http', '--wsgi-file', f'{__file__}', '--callable', 'application'],
        stdout=sys.stdout,
        stderr=sys.stdout,
        text=True,
    )
