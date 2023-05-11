from .views import TypeView, not_found

from .views import index, About, contact
from typing import TypedDict


class TypeRoute(TypedDict):
    path: str
    endpoint: TypeView


routes: TypeRoute = {
    '/': index,
    '/about/': About(),
    '/contact/': contact,
}
