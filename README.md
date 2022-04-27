## Project setup
django-admin startproject exile_tools_poc
cd exile_tools_poc
manage.py startapp gemplanner

## F-Strings

## Models
Datenbank-Models:
```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
````

## Apps
Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.
````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gemplanner_poc.apps.GemplannerPocConfig',
]
````

## DB Migrations
Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.

````
>>> from gemplanner_poc.models import POESkillGem
KeyboardInterrupt
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
vscode ➜ /workspace/exile_tools_poc $ ./manage.py migrate 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, gemplanner_poc, sessions
Running migrations:
  Applying gemplanner_poc.0001_initial... OK
vscode ➜ /workspace/exile_tools_poc $ ./manage.py shell
Python 3.10.4 (main, Apr  7 2022, 03:15:56) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from gemplanner_poc.models import POESkillGem
>>> POESkillGem.objects.all()
<QuerySet []>
````