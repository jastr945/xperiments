FROM python:3.6

WORKDIR /usr/src/app
RUN pip install django uwsgi psycopg2-binary social-auth-app-django requests ipdb
COPY . .
RUN mkdir /var/lib/kubebooks/
EXPOSE 80
CMD . /usr/src/app/startserver.sh
# CMD sleep 20000000000
