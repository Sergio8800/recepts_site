
Шаги развертывания:
добавляем завистимости в проект:
pip freeze >require.txt

регистарация на сайте:
www.pythonanywhere.com/

в консоле пайтон ресурса:
https://www.pythonanywhere.com/user/s11u11n/consoles/33784724/

клонируем проект с гитхаба:
bash console: git clone https://github.com/Sergio8800/GBpractic.git

добавляем виртуальное окружение:
mkvirtualenv --python=/usr/bin/python3.10 virtualenv

переходим в папвку проекта(ls, cd)
устанавливаем зависимости.
pip install -r require.txt

Working directory:
/home/s11u11n/

Virtualenv:
/home/s11u11n/.virtualenvs/virtualenv/

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/s11u11n/mysite/mysite/settings.py'
## and your manage.py is is at '/home/s11u11n/mysite/manage.py'
path = '/home/s11u11n/GBpractic'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

собираем статические файлы:
python manage.py collectstatic

URL         Path
/static/    /home/s11u11n/GBpractic/static

ALLOWED_HOSTS = ['127.0.0.1',
                 's11u11n.pythonanywhere.com ']