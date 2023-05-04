from .views import TypeView, not_found

from .views import index, Page, contact
from typing import TypedDict


class TypeRoute(TypedDict):
    path: str
    endpoint: TypeView


routes: TypeRoute = {
    '/': index,
    '/page/': Page(),
    '/contact/': contact,
}
