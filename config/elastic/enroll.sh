#!/usr/bin/env bash -x
# Derived from https://aws.amazon.com/blogs/opensource/add-ssl-certificates-open-distro-for-elasticsearch/.

# Generate our root certificate.
openssl genrsa -out elastic-root-ca.key 4096
openssl req -x509 -new -key elastic-root-ca.key -nodes -subj "/CN=production-deployment CA" -sha256 -out elastic-root-ca.pem

# Generate our node's certificate set.
openssl genrsa -out elastic-node-pkcs12.key 4096
# Ensure it is in the PKCS#5 v1.5 format for JDK usage.
openssl pkcs8 -v1 "PBE-SHA1-3DES" -in elastic-node-pkcs12.key -topk8 -out elastic-node.key -nocrypt

# We give a common name of "elastic" as this matches our container's name.
openssl req -new -key elastic-node.key -out elastic-node.csr -nodes -subj "/CN=elastic"
openssl x509 -req -in elastic-node.csr -CA elastic-root-ca.pem -CAkey elastic-root-ca.key -CAcreateserial -out elastic-node.pem -sha256

chmod 0600 elastic-node.pem elastic-node.key elastic-root-ca.pem

# Ensure these files are accessible by containers.
chown 1000:1000 *.pem *.key

printf "\nDone, certificates prepared.\n"