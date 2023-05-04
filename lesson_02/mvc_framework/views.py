from typing import Callable

from .request import Request
from .response import Response
from .templator import render, render_from_line

TypeView = Callable[[Request], tuple[str, str | bytes]]


def index(request: Request) -> tuple[str, str]:
    status = '200 OK'
    context = {'key': 'value'}
    return status, render('index.html', context=context)


class Page:

    def __call__(self, request: Request) -> tuple[str, str]:
        status = '200 OK'
        context = {'key': 'value'}
        return status, render('page.html', context=context)


def not_found(request: Request) -> tuple[str, str]:
    status: str = '404 NOT FOUND'
    body: str = 'NOT FOUND 404'
    return status, body


def contact(request: Request):
    status = '200 OK'
    context = {}

    if request.method == 'POST':
        # form = NameForm(request.POST)

        # полученная форма
        print('>>>', request.request.query_string)
        print('>>>', request.request_body)
        return status, render_from_line('Thanks!')

    return status, render('contact.html', context=context)
