FROM python:3.6

WORKDIR /usr/src/app
RUN pip install django uwsgi psycopg2
COPY . .
RUN mkdir /var/lib/kubebooks/
EXPOSE 80
CMD . /usr/src/app/startserver.sh
