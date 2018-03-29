web:python manage.py runserver
web:python manage.py collectstatic --noinput;
web: gunicorn livewire.wsgi --log-file -
heroku ps:scale web=1
