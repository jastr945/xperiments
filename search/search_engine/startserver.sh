sleep 30
python3 manage.py migrate
python3 manage.py loaddata fixturefile.json
uwsgi --chdir=./ --module=search_engine.wsgi:application --env DJANGO_SETTINGS_MODULE=search_engine.settings --socket=/tmp/search_engine.sock --master --http :80
