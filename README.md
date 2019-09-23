# Django eMenu project

# **1. database setup:**

sudo -u postgres psql (psql -U postgres in Windows)

create database restaurant;

create user admin with encrypted password 'enchiladas';

grant all privileges on database restaurant to admin;

alter role admin createdb;

# **2. django project setup:**

git clone https://github.com/fannyhub/eRestaurant.git

install venv (with Python3.7 interpreter) - e.g. virtualenv --python=python3.7 venv

activate it with source venv/bin/activate (Linux) or venv/Scripts/activate (Windows)

pip install -r requirements.txt

python manage.py makemigrations menu

python manage.py migrate

populate db with sample data: python manage.py loaddata sample_data.json

create Django superuser to enter Django admin with python manage.py createsuperuser

you might precede this command with winpty on Windows


# **3. run the project...**

python manage.py runserver - locally you can access the project at 127.0.0.1:8000

# **... 4. or test it:**

pytest


# **CREDITS:**
Background photo by Brooke Lark on Unsplash (free picture)