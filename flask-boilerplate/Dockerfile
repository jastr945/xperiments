FROM python:3.6
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN flask initdb
CMD ["uwsgi",  "--ini", "uwsgi.ini"]
