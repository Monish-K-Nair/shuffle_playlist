FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements

RUN apk add --update --no-cache postgresql-client
RUN apk --no-cache add musl-dev linux-headers g++

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install --upgrade pip
RUN pip install -r /requirements/base.txt

RUN apk del .tmp-build-deps
RUN apk add graphviz ttf-freefont

RUN mkdir /app

COPY ./app /app

WORKDIR /app/dj_playlist
RUN adduser -D demo-user

USER demo-user
