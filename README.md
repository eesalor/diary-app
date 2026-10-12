# Diary App 

The application is created for the course Cyber Security Base: Project I.

The application is based on the Django framework, and the starter website is partly created by using the Django app
[tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial04/).

## Installation

1. Clone the git repository:
```
git clone https://github.com/eesalor/diary-app.git
```

2. Go to directory `diary-app` and create a virtual environment:
```
python -m venv venv
```
3. Activate the virtual environment:
```
source venv/bin/activate
```

4. When the virtual environment is activated, install following dependencies:
```
pip install django requests django-session-timeout django-auto-logout pytz python-dotenv
```
5. Go to directory `diary-app/mysite` and create a file `.env`.

```
touch .env
```
6. Create SQL database by running migrations:
```
python manage.py migrate
```

During the installation, a SQL database `db.sqlite3` is created in the directory `diary-app/mysite`.


## Start the application

Go to directory `diary-app/mysite` and start the application:
```
python manage.py runserver
```

The application starts at local domain, http://127.0.0.1:8000/ by default.
You can also run the application at different port, for example at 9000:
```
python manage.py runserver 9000
```

## How to create admin

It is possible to create admin user:
```
python manage.py createsuperuser
```
When the application is running, admin login page can be accessed at http://127.0.0.1:8000/admin


