# Elastic-specific configuration

It's highly encouraged to use TLS for connecting from a client to Elasticsearch in general.
One might even go as far as saying it is mandated.
Indeed, we mandate this within production-deployment.

You'll need a root certificate by the name `elastic-root-ca.pem` and node-specific certificates (`elastic-node.{key,pem}`) to serve.
The node-specific certificates must be PKCS#5 v1.5 or the JDK will break.

Alternatively, ensure OpenSSL is installed and run `enroll.sh` to have these automatically created.