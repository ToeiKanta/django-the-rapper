# django-the-rapper
## command usage
```
// export virtual env to file
$ pip freeze > requirements.txt

// import virtual env from file
$ virtualenv <env_name>
$ source <env_name>/bin/activate
(<env_name>)$ pip install -r path/to/requirements.txt

// make database migration
$ python manage.py makemigrations

// migrate database
$ python manage.py migrate
```