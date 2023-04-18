FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

WORKDIR /logs/bookmarks
RUN echo "" > my-log.json

WORKDIR /bookmarks-api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "--workers=4" , "--bind", "0.0.0.0:8500", "wsgi:app"]