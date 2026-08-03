import os

# Primary config for cam-server
db_url = ""

# Used to secure the web panel.
secret_key = ""

# Sentry configuration for error logging.
use_sentry = True
sentry_dsn = ""

# EULA text, presented upon first launch of channel.
# You may wish to change this to read from a file.
with open("/home/server/conf/eula.txt") as eula_file:
    eula_text = eula_file.read()

# OpenID Connect configuration
oidc_redirect_uri = ""
oidc_client_secrets_json = {
    "web": {
        "client_id": "",
        "client_secret": "",
        "auth_uri": "",
        "token_uri": "",
        "userinfo_uri": "",
        "issuer": "",
        "redirect_uris": [oidc_redirect_uri],
    }
}
oidc_logout_url = ""