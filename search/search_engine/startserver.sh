# echo "host all all 172.18.0.4/16 md5" >> /etc/postgresql/9.5/main/pg_hba.conf
python3 manage.py migrate
uwsgi --chdir=./ --module=search_engine.wsgi:application --env DJANGO_SETTINGS_MODULE=search_engine.settings --socket=/tmp/search_engine.sock --master --http :80
