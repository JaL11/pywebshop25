# Welcome to pyWeb 2025 project

## Install instructions for devs (on linux)

`python -m venv .venv`

source .venv/bin/activate

`python pip install -r requirements.txt`

`python manage.py runserver`

## Create a new app

`django-admin startapp <appname>`

## Branching and merge requests

I created dev for branch seperation for individual development

Not sure we'll use two different branches but
*IMPORTANT*
development must be done in seperate branches

### Workflow for linux

`git pull`

`git checkout -b feature_<name>`

`git push`

(can also be done in web-interface)
`git merge feature_<name> dev`

`git push`

---

## Deployment Checklist for pythonanywhere

### WebApp setup

- Set URL for static
  - `URL = /static/`
  - `Directory = /home/pyWebShop25/static_production`
- Set URL for media
  - `URL = /media/`
  - `Directory = /home/pyWebShop25/media`

### Pre deploy steps

- run `./startup.sh` this sets up the production environment and makes sure database migrations are in place
- make sure `.env` has needed vars set
- as saftey check run `python manage.py check --deploy`

### make sure this is in the `/var/www/pywebshop25_eu_pythonanywhere_com_wsgi.py` file

``` python
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/pyWebShop25/mysite/mysite/settings.py'
# and your manage.py is is at '/home/pyWebShop25/mysite/manage.py'
path = '/home/pyWebShop25/pywebshop25'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'webshop.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### example `.env`

``` bash
PRODUCTION_ENV=True # or False
DEBUG=False # or True
DJANGO_LOGLEVEL=info
DJANGO_ALLOWED_HOSTS=pyWebShop25.eu.pythonanywhere.com,127.0.0.1 #remove 127.0.0.1 in prod
#DATABASE_ENGINE=mysql #for mysql
MYSQL_DB_NAME=pywebshop
MYSQL_DB_UNAME=webshopdb #check pythonanywhere config
MYSQL_DB_PASSWORD=<pythonanywhere for pw i think>
MYSQL_DB_URL= #if using pythonanywhere mysqldb service: username.mysql.eu.pythonanywhere-services.com
#run command in startup.sh for secretkey
#SECRET_KEY=.....
```
