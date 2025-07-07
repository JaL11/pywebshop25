# Welcome to pyWeb 2025 project 

## Install instructions for devs

```
python -m venv .venv

source .venv/bin/activate

python pip install -r requirements.txt


python manage.py runserver
```

## Create a new app

`django-admin startapp <appname>`

## Branching and merge requests

I created dev for branch seperation for individual development

Not sure we'll use two different branches but 
*IMPORTANT*
development must be done in seperate branches

### Workflow

`git pull`

`git checkout -b feature_<name>`

`git push`

(can also be done in web-interface)
`git merge frature_<name> dev`

`git push`
