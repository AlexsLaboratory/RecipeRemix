FROM python:3.9-alpine

WORKDIR /tests
COPY ./app/tests/selenium ./app
RUN apk add --update --no-cache --virtual .tmp gcc python3-dev libc-dev linux-headers
RUN pip install --upgrade pip
RUN pip install --no-cache-dir selenium~=4.1.3 pytest~=7.1.1
RUN apk del .tmp