FROM python:3.9-alpine

WORKDIR /tests
COPY ./app/tests/selenium ./app
COPY ./docker/selenium-tests/pytest.ini ./
COPY ./requirements.txt ./
RUN apk add --update --no-cache --virtual .tmp gcc python3-dev libc-dev libffi-dev linux-headers
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .tmp