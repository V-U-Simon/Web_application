from dataclasses import dataclass, field
from typing import Iterable

from .config import ENCODING


@dataclass
class Response:
    status: str = None
    body: Iterable[bytes]
    headers: list[tuple[str, str]] = field(default_factory=lambda: [('Content-Type', 'text/plain')])

    @property
    def body(self) -> Iterable[bytes]:
        if isinstance(self._body, bytes):
            return [self._body]
        return [self._body.encode(ENCODING)]

    @body.setter
    def body(self, value: str | bytes):
        self._body = value


if __name__ == '__main__':
    # some test
    responce = Response('404 not Found', 'some content')
    print(responce.body)
