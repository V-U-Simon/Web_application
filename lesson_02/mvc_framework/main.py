from loguru import logger
from dataclasses import dataclass
from typing import Callable, Iterable
from functools import partial

from .request import Request
from .response import Response
from .routers import routes, TypeRoute
from .views import TypeView, not_found


class Application:
    routes: TypeRoute = routes

    @logger.catch()
    def __call__(self, environ, start_response):
        # метод запроса опредяется в объекте Request с помощью фукнции-заплнителя объекта (fill_request)
        request = Request(environ)

        view: TypeView = self.routes.get(request.path, not_found)
        status, body = view(request)

        response = Response(status=status, body=body)
        start_response(response.status, response.headers)

        return response.body
