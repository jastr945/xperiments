python3.6 manage.py makemigrations
python3.6 manage.py migrate
uwsgi --chdir=./ --module=kubebooks.wsgi:application --env DJANGO_SETTINGS_MODULE=kubebooks.settings --socket=/tmp/kubebooks.sock --master --http :80
