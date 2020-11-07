FROM nginx:1.19-alpine

# Used for templating.
# Must be present during build.
ARG FQDN
ENV FQDN=${FQDN}

COPY default.conf /etc/nginx/conf.d/default.conf
COPY main.conf.template /etc/nginx/templates/main.conf.template
