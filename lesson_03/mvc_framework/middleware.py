# from pprint import pprint
# from .config import ENCODING
# import json
# from loguru import logger
# from .request import Request, RequestMethods

# @Request.register_filler
# def fill_request(request: Request) -> None:
#     """ Заполнение объекта запроса """

#     method =
#     request.method = RequestMethods(method)

#     logger.success(f'request is filled successfully')

# def fill_request_for_get(request: Request) -> None:
#     environ: dict[str, str] = request.environ

#     query_string = environ.get('QUERY_STRING', None)
#     if query_string:
#         request.query_string: dict[str, str] = parse_query_string(query_string)

# def fill_request_for_post(request: Request) -> None:
#     environ: dict[str, str] = request.environ

#     request_body_size = int(environ.get('CONTENT_LENGTH', 0))
#     if request_body_size:
#         request.content_type = environ.get('CONTENT_TYPE')
#         request_body: bytes = environ['wsgi.input'].read(request_body_size)
#         request.request_body: dict[str, str] = parse_input_bytes(request_body)
#         logger.info(request.request_body)

# def parse_query_string(query_string: str) -> dict[str, str]:
#     try:
#         query_string = dict(pair.split('=') for pair in query_string.split('&'))
#         logger.success(f'Parse is successful: {query_string}')
#         return query_string
#     except ValueError as e:
#         logger.error(f'Parse string: {query_string!r} is failed')

# def parse_input_bytes(input_bytes: bytes) -> dict[str, str]:
#     try:
#         query_string = input_bytes.decode(ENCODING)
#     except ValueError as e:
#         logger.error(f'Parse butes: {query_string!r} is failed')

#     query_string = query_string.replace('{', '').replace('}', '').replace('"', '').replace(':', '=')
#     return dict(parse_query_string(query_string))

# if __name__ == '__main__':
#     # little test
#     parse_query_string('key_1=1&key_2=2')
#     parse_query_string('')  # exception
#     parse_query_string('wrong format')  # exception
#     parse_input_bytes(b'key_1=1&key_2=2')
#     parse_input_bytes('key_1=1&ключ_2=2'.encode('utf-8'))
#     parse_input_bytes(b'')