# django-the-rapper

this repository is inspired by [dookie1983/the-rapper-api-workshop](https://github.com/dookie1983/the-rapper-api-workshop/)

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

// run server
$ python manage.py runserver

// create model 
$ django-admin startapp <model_name>
```