import sys
import subprocess
from wsgiref.simple_server import make_server

from mvc_framework.main import Application

application = Application()

if __name__ == '__main__':
    # НЕОБХОДИМО ЗАПУСКУТЬ ИЗ ПАПКИ КОТОРАЯ СОДЕРЖИТЬ ТЕКУЩИЙ ФАЙЛ, для корректной работы шаблонов
    print('##############################################')
    print('running application on http://localhost:8080')
    print('##############################################')
    # # uwsgi
    # process_res = subprocess.run(
    #     [f'uwsgi --socket :8080 --protocol=http --wsgi-file {__file__} --callable application'],
    #     shell=True,
    #     stdout=sys.stdout,
    #     stderr=sys.stdout,
    #     text=True,
    # )

    # Запросы:
    # http -v GET localhost:8080/page?key_1=val_1&key_2=val_2
    # http -v POST localhost:8080/page 'key_1=val_1&key_2=val_2'
    with make_server('', 8080, application) as httpd:
        httpd.serve_forever()