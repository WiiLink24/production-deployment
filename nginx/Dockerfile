FROM nginx:alpine

COPY default.conf /etc/nginx/conf.d/default.conf
COPY templates/*.template /etc/nginx/templates/
COPY static/ /var/www/
