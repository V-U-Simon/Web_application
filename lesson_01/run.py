import sys
import subprocess

from mvc_framework import urls
from mvc_framework.middleware import fronts
from mvc_framework.main import Application

application = Application(urls.routes, fronts)

if __name__ == '__main__':
    print('##############################################')
    print('running application on http://localhost:8080')
    print('##############################################')
    process_res = subprocess.run(
        [f'uwsgi --socket :8080 --protocol=http --wsgi-file {__file__} --callable application'],
        shell=True,
        stdout=sys.stdout,
        stderr=sys.stdout,
        text=True,
    )
