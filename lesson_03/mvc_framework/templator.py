from jinja2 import Template
from pathlib import Path
from .config import ENCODING, TEMPLATE_FOLDER

from loguru import logger

# относительный путь к папке с шаблонами


def render_from_line(template_line: str, context: dict) -> str:
    """ Сформировать шаблон из текста """
    template = Template(template_line)
    return template.render(**context)


def render(template_file: str, context: dict) -> str:
    """ Сформировать шаблон из файла """

    template_file = TEMPLATE_FOLDER / template_file
    if not template_file.exists():
        logger.error(f'Template file (or templates folder) is not exists: {template_file}')
        raise FileExistsError(f'{template_file}')

    with open(template_file, 'r', encoding=ENCODING) as f:
        template = Template(f.read())
        return template.render(**context)


if __name__ == '__main__':
    # some test
    res = render_from_line('Hello {{ name }}', context={'name': 'John Doe'})
    print(res)

    res = render('page.html', context={'name': 'John Doe'})
    print(res)