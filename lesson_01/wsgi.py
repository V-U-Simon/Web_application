import sys
import subprocess


def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
    ]
    body = 'hello world 1222'.encode('utf-8')

    start_response(status, headers)
    return [body]


if __name__ == '__main__':

    process_res = subprocess.run(
        [f'uwsgi', '--socket', ':8080', '--protocol=http', '--wsgi-file', f'{__file__}', '--callable', 'application'],
        stdout=sys.stdout,
        stderr=sys.stdout,
        text=True,
    )
