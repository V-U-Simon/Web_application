from jinja2 import Template
from pathlib import Path

TEMPLATE_FOLDER = 'templates'


def render_from_line(template_line: str, context: dict):
    """ Сформировать шаблон из текста """
    template = Template(template_line)
    return template.render(**context)


def render(template_file, context: dict):
    """ Сформировать шаблон из файла """

    template_file = Path.cwd() / TEMPLATE_FOLDER / template_file

    with open(template_file, 'r') as f:
        template = Template(f.read())
        return template.render(**context)


# if __name__ == '__main__':
#     # some test

#     res = render_from_line('Hello {{ name }}', context={'name': 'John Doe'})
#     print(res)

#     template_file = Path.cwd() / 'templates' / 'stub.html'
#     res = render(template_file, context={'name': 'John Doe'})
#     print(res)