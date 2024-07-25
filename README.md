# brain-agriculture
Teste - Brain Agriculture

## Setup

Create virtualenv:

`python3 -m venv venv`

Active virtualenv

`source venv/bin/activate`

Install requirements.txt

`pip install -r requirements.txt`


## Load data

Create database

`python manage.py migrate`

Load fixtures

`python manage.py loaddata initial_data.json`


# Run

`python manage.py runserver`


# Test

`pytest`
