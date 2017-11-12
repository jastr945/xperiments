python3 manage.py migrate
uwsgi --chdir=./ --module=search_engine.wsgi:application --env DJANGO_SETTINGS_MODULE=search_engine.settings --socket=/tmp/search_engine.sock --master --http :80s
