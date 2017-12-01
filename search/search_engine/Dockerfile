FROM python:3.6

WORKDIR /usr/src/app
RUN pip install -U pip django Pillow uwsgi WhiteNoise elasticsearch-dsl django-elasticsearch-dsl django-tinymce mysqlclient
COPY . .
RUN python3 manage.py collectstatic --noinput
EXPOSE 80
CMD . /usr/src/app/startserver.sh
