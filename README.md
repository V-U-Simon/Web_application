# Architecture examples project

### This is a test project demonstrating:

- MVC (Model-View-Controller) architecture pattern in web application development.
- page controller
- front controller

### Project structure

This test project implements a simple web application architecture patterns.\n
Here is the project structure:

```
├── app.py
├── ... in progress
└── README.md
```

### How to run the application

To run the application, you need to install the required packages listed in pyproject.toml using poetry.

```
poetry install
poetry shell
```

Next, you can run application by wsgi.py script.

```
uwsgi --socket 0.0.0.0:8080 --protocol=http --module wsgi:application
```
