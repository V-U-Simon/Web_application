from abc import ABC
from dataclasses import dataclass
import functools
from pprint import pprint
from typing import Callable, ClassVar
from enum import Enum
from .config import ENCODING
from loguru import logger
from sys import stdout


class Request:

    def __init__(self, environ: dict[str, str]):
        """ Default constructor using GET method """

        self.environ = environ
        self.method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        self.path: str = path if path.endswith('/') else path + '/'

        # вызов обработчика соответствующиего определенному методу
        request_handler = getattr(self, self.method)
        request_handler()

    def GET(self):
        self.query_string = self.parse_query_string(self.environ['QUERY_STRING'])

    def POST(self):
        self.content_type: str = self.environ['CONTENT_TYPE']
        self.content_length = int(self.environ.get('CONTENT_LENGTH', 0))

        if self.content_length:
            self.data: bytes = self.environ['wsgi.input'].read(self.content_length)
        else:
            self.data: bytes = b''

        self.query_string = self.parse_wsgi_input_data(self.data)

    def parse_query_string(self, query_string):
        try:
            if query_string:
                query_string = dict(pair.split('=') for pair in query_string.split('&'))
            logger.info(f'Parse string: {query_string!r}')
            return query_string

        except ValueError as e:
            logger.error(f'Parse string: {query_string!r} is failed')

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        try:
            query_string = data.decode(ENCODING)
        except ValueError as e:
            logger.error(f'Parse bytes: {query_string!r} is failed')
        return self.parse_query_string(query_string)

    # fillers: ClassVar[list[Callable]] = []

    # def __post_init__(self) -> None:
    #     cls = self.__class__

    #     for filler in cls.fillers:
    #         filler(self)

    # @classmethod
    # def register_filler(cls, func):
    #     cls.fillers.append(func)
    #     return func


if __name__ == '__main__':
    # simple test case

    environ = {
        'PATH_INFO': '/this_is_some_path',
        'REQUEST_METHOD': 'GET',
        'QUERY_STRING': 'key_1=1&key_2=2',
        'REMOTE_ADDR': '127.0.0.1',
        'REQUEST_URI': '/this_is_some_path?key=1&key=2',  # CGI-like переменные
        'wsgi.input': b'key_1=1&key_2=2'
    }

    r = Request(environ=environ)

    print(r.path)
    print(r.method)
