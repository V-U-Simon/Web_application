from jinja2 import Template
from pathlib import Path

TEMPLATE_FOLDER = 'templates'


def render_from_line(template_line: str, context: dict) -> str:
    """ Сформировать шаблон из текста """
    template = Template(template_line)
    return template.render(**context)


def render(template_file: str, context: dict) -> str:
    """ Сформировать шаблон из файла """

    template_file = Path.cwd() / TEMPLATE_FOLDER / template_file
    print(template_file)
    print('/Users/macbook/Code/Education/Web_application/lesson_02/templates')
    print(Path.exists(template_file))

    with open(template_file, 'r') as f:
        template = Template(f.read())
        return template.render(**context)


if __name__ == '__main__':
    # some test
    res = render_from_line('Hello {{ name }}', context={'name': 'John Doe'})
    print(res)

    res = render('page.html', context={'name': 'John Doe'})
    print(res)