FROM amazon/opendistro-for-elasticsearch:1.13.2

USER root

# Remove all demo certificates.
RUN rm /usr/share/elasticsearch/config/*.pem

# Prefer our own.
COPY elastic-node.key /usr/share/elasticsearch/config
COPY elastic-node.pem /usr/share/elasticsearch/config
COPY elastic-root-ca.pem /usr/share/elasticsearch/config

# Copy in our own elasticsearch.yml.
COPY elasticsearch.yml /usr/share/elasticsearch/config

# Ensure the running Elasticsearch user can access these keys.
RUN cd /usr/share/elasticsearch/config && \
    chown elasticsearch:root elastic-node.key elastic-node.pem elastic-root-ca.pem elasticsearch.yml

USER elasticsearch