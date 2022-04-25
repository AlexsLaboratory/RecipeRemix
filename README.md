# Webpage Application - Recipe Remix 

A web application that allows users to input diet restrictions, food preferences, and current foods they have to produce a list of favorable recipes.

## Setup
### Downloads
 - [Docker](https://www.docker.com/get-started/)

### Development
We have made contributing to our project very easy because we use containers for each aspect of our application. In order to get it up and running all you have to do is run `docker-compose up -d --build` from the root of the project. Now you can go to `localhost:8000` to view the application. See that was soo easy.

### Production
This is going to be a little bit more complicated as we have Certbot which generates our SSL certificates. The issue is that Certbot adds a file to the website in the `.well-kown` directory. Within the proxy (Nginx) configureation it is going to redirect any traffic from port 80 (insecure traffic) to port 443 (secure traffic) this is the recomendated way to do things now adays. If there is no SSL certificate already created than the configuration is going to reference a file that does not exist yet and the server will not start. The issue is that the server needs to start in order to have certbot generate and verify the SSL cert. The way to get around this is to go into the `docker/proxy/default.conf` file and move lines `39-42` and replace lines `18-20`. From there comment out lines `23-43`. This will disable SSL completely and allow it to run with out failing.

The final thing to do is to run and replace `DOMAINNAME.SOMETHING` with your actual domain name `docker-compose -f docker-compose-deploy.yml run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d DOMAINNAME.SOMETHING`. Within the `default.conf` you will also have to replace any reference to `recipe-remix.tech` with the domain of your choosing. Once that command succeeds you can go back to the first step and undo what you did in order to re-enable SSL and your site should then be fully functional.

The last thing to do is run `docker-compose -f docker-compose-deploy.yml up -d --build`
