FROM node:17
WORKDIR /app
COPY package*.json ./
COPY gulpfile.js ./
RUN npm install
RUN npm install -g gulp-cli
COPY . .
RUN gulp buildStyles

FROM python:3.9-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .