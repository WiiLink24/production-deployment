import os

# Primary config for cam-server
db_url = f"postgresql://{os.getenv('DEMAE_DB_USER')}:{os.getenv('DEMAE_DB_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('DEMAE_DB_DATABASE')}"

# Used to secure the web panel.
secret_key = os.getenv("DEMAE_SECRET_KEY")

# Sentry configuration for error logging.
use_sentry = True
sentry_dsn = os.getenv("DEMAE_SENTRY_DSN")

# EULA text, presented upon first launch of channel.
# You may wish to change this to read from a file.
with open("/home/server/conf/eula.txt") as eula_file:
    eula_text = eula_file.read()

# OpenID Connect configuration
oidc_redirect_uri = os.getenv("DEMAE_OIDC_REDIRECT_URL")
oidc_client_secrets_json = {
    "web": {
        "client_id": os.getenv("DEMAE_OIDC_CLIENT_ID"),
        "client_secret": os.getenv("DEMAE_OIDC_CLIENT_SECRET"),
        "auth_uri": os.getenv("DEMAE_OIDC_AUTH_URL"),
        "token_uri": os.getenv("DEMAE_OIDC_TOKEN_URL"),
        "userinfo_uri": os.getenv("DEMAE_OIDC_USERINFO_URL"),
        "issuer": os.getenv("DEMAE_OIDC_ISSUER"),
        "redirect_uris": [oidc_redirect_uri],
    }
}
oidc_logout_url = os.getenv("DEMAE_OIDC_LOGOUT_URL")