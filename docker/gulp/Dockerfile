FROM node:17
WORKDIR /app
COPY package*.json ./
COPY gulpfile.js ./
RUN npm install
RUN npm install -g gulp-cli
COPY . .