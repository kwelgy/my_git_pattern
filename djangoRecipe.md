## Django recipe

Create virtual env

Install django

```django-admin startproject mysite```

```python manage.py startapp polls```

Create urls.py in app foilder

Point root URLconf at polls.urls using include

```$python manage.py migrate``` - to build database tables

```python manage.py makemigrations polls``` - prepare new app for migration

```python manage.py sqlmigrate polls 0001``` - see what django thinks it needs to do
