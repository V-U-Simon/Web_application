def fill_request(request: dict):
    request['key'] = 'value'


def fill_request_2(request: dict):
    request['other_key'] = 'other_value'


fronts = [fill_request, fill_request_2]
