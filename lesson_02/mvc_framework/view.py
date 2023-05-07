from .templator import render


def index(request):
    status = '200 OK'
    context = {'key': 'value'}
    return status, render('index.html', context=context)


class Page:

    def __call__(self, request):
        status = '200 OK'
        context = {'key': 'value'}
        return status, render('page.html', context=context)
