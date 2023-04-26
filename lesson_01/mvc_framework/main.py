from dataclasses import dataclass
from typing import Callable, Iterable
from functools import partial


def not_found(request):
    status = '404 NOT FOUND'
    body = 'NOT FOUND 404'
    return status, body


@dataclass
class Response:
    headers: list[tuple[str, str]]
    status: str = None
    body: Iterable[bytes] = None  # todo: descriptor with ecripting


class Path:

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, path):
        # check slash in path
        print('__set__')
        path: str = path if path.endswith('/') else path + '/'
        instance.__dict__[self.name] = path

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]


@dataclass
class Request:
    path: Path = Path()

    def __init__(self, environ: dict):
        [setattr(self, key, value) for key, value in environ.items()]
        self.path = self.PATH_INFO


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        response = Response(headers=[('Content-Type', 'text/plain')],)
        request = Request(environ)

        for front in self.fronts:
            front(request)

        if request.path in self.routes:
            view: Callable[[Request], tuple[str, str]] = self.routes[request.path]
        else:
            view = not_found

        response.status, response.body = view(request)
        start_response(response.status, response.headers)
        return [response.body.encode('utf-8')]
