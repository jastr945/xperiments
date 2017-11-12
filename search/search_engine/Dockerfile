FROM python:3.6

WORKDIR /usr/src/app
RUN pip install django Pillow uwsgi WhiteNoise elasticsearch-dsl django-elasticsearch-dsl django-tinymce pyenchant 
COPY . .
RUN python3 manage.py collectstatic --noinput

EXPOSE 80
CMD . /usr/src/app/startserver.sh
