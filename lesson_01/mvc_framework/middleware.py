from lesson_01.mvc_framework.main import Request


def fill_request(request: Request):
    setattr(request, 'key', 'value')


def fill_request_2(request: Request):
    setattr(request, 'key_2', 'value_2')


fronts = [fill_request, fill_request_2]
