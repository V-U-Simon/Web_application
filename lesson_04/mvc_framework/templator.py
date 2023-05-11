import os
from jinja2 import Template, select_autoescape, Environment
from jinja2 import FileSystemLoader, ChoiceLoader
from pathlib import Path

from .config import TEMPLATE_FOLDER

loaders = (
    FileSystemLoader(Path(__file__).parent / TEMPLATE_FOLDER),  # config_loader: .../mvc_framework/{TEMPLATE_FOLDER}
    FileSystemLoader(Path(__file__).parent.parent / 'templates'),  # default_loader: .../mvc_framework/../templates
)

autoescaping = select_autoescape(
    # enabled_extensions=('txt',),  # 🌝 включить  для файлов с расширениями: 'html',
    disabled_extensions=('html',),  # 🌚 выключить для файлов с расширениями: 'txt', 
    default_for_string=False,  # 📦 для str
    default=False)

env = Environment(
    loader=ChoiceLoader(loaders),
    autoescape=autoescaping,
    extensions=[],
)


def render(template_file: str, context: dict) -> str:
    """ Сформировать шаблон из файла """
    template: Template = env.get_template(template_file)
    return template.render(**context)


if __name__ == '__main__':
    # some test

    res = render('base.html', context={'name': 'John Doe'})
    print(res)