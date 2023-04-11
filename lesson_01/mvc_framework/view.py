from .templator import render


def index(request):
    status = '200 OK'
    body = 'index'
    return status, render('templates/stub.html', request)


class Info:

    def __call__(self, request):
        status = '200 OK'
        body = 'info'
        return status, body
