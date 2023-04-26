from .view import index, Page

routes: dict[str, callable] = {
    '/': index,
    '/page/': Page(),
}
