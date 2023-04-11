from jinja2 import Template
from pathlib import Path


def render_from_line(template, context: dict):
    template = Template(template)
    return template.render(**context)


def render(template, context: dict):
    with open(template, 'r') as f:
        template = Template(f.read())
        return template.render(**context)


if __name__ == '__main__':
    # some test

    res = render_from_line('Hello {{ name }}', context={'name': 'John Doe'})
    print(res)

    template_file = Path.cwd() / 'templates' / 'stub.html'
    res = render(template_file, context={'name': 'John Doe'})
    print(res)