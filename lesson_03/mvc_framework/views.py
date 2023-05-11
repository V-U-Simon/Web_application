from typing import Callable
from jinja2 import Environment, Template, select_autoescape

from loguru import logger

from .request import Request
from .response import Response
from .templator import render

TypeView = Callable[[Request], tuple[str, str | bytes]]


def not_found(request: Request) -> tuple[str, str]:
    status: str = '404 NOT FOUND'
    body: str = 'NOT FOUND 404'
    return status, body


def index(request: Request) -> tuple[str, str]:
    status = '200 OK'
    context = {'key': 'value'}
    return status, render('index.html', context=context)


class About:

    def __call__(self, request: Request) -> tuple[str, str]:
        status = '200 OK'
        context = {'key': 'value'}
        return status, render('about.html', context=context)


def contact(request: Request):
    status = '200 OK'
    context = {'country': '<h1>Sparta!</h1>'}
    template = 'this is {{ country}}'

    if request.method == 'POST':
        # form = NameForm(request.POST)

        # полученная форма
        # logger.info('>>>', request.method)
        # logger.info('>>>', request.query_string)
        return status, ('<h1>Thanks!</h1>',)

    return status, render('contact.html', context=context)
