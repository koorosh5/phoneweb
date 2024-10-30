#!/bin/bash

python manage.py migrate

# Run tests (optional)
python manage.py test

# Run the development server
python manage.py runserver