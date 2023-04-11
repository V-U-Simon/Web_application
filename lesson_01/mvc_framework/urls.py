from .view import index, Info

routes: dict[str, callable] = {
    '/': index,
    '/info': Info(),
}
