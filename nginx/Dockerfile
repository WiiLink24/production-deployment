FROM nginx:1.19-alpine

# Used for templating.
# Must be present during build.
ARG FQDN
ARG NGINX_BASE_DOMAIN
ENV FQDN=${FQDN}
ENV NGINX_BASE_DOMAIN=${NGINX_BASE_DOMAIN}

COPY default.conf /etc/nginx/conf.d/default.conf
COPY main.conf.template /etc/nginx/templates/main.conf.template
COPY demae.conf.template /etc/nginx/templates/demae.conf.template
