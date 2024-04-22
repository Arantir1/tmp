# syntax=docker/dockerfile:1

FROM python:alpine

WORKDIR /django-app

RUN apk add libpq-dev
RUN apk add build-base

COPY . . 
RUN pip3 install -r requirements.txt

CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:8000"]
