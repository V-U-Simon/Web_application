from dataclasses import dataclass
import functools
from pprint import pprint
from typing import Callable, ClassVar
from enum import Enum
from loguru import logger


class RequestMethods(Enum):
    GET = 'GET'
    POST = 'POST'


@dataclass
class Request:
    environ: dict[str, str]
    fillers: ClassVar[list[Callable]] = []

    def __post_init__(self) -> None:
        cls = self.__class__

        for filler in cls.fillers:
            filler(self)

    @classmethod
    def register_filler(cls, func):
        cls.fillers.append(func)
        return func


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
