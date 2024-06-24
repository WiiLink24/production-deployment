# Please ensure this file has its options synchronized with the example in room-server.
import os

# Primary config for room-server
db_url = f"postgresql://{os.getenv('ROOM_DB_USER')}:{os.getenv('ROOM_DB_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('ROOM_DB_DATABASE')}"

# Used as the base domain within first.bin.
root_domain = os.getenv("NGINX_BASE_DOMAIN")
# TODO: make toggleable once possible
root_https_enabled = False
# We assume we are being proxied with the default Compose definition.
root_separate_subdomain = True


# Used to secure the web panel.
secret_key = os.getenv("ROOM_SECRET_KEY")

# Sentry configuration for error logging.
use_sentry = True
sentry_dsn = os.getenv("ROOM_SENTRY_DSN")

use_s3 = False
r2_account_id = os.getenv("R2_ACCOUNT_ID")
r2_bucket_name = os.getenv("R2_BUCKET_NAME")
s3_connection_url = os.getenv("S3_CONNECTION_URL")
s3_access_key_id = os.getenv("S3_ACCESS_KEY_ID")
s3_secret_access_key = os.getenv("S3_SECRET_ACCESS_KEY")

url1_cdn_url = os.getenv("URL1_CDN_URL")

ds_rsa_key_path = os.getenv("DS_RSA_KEY_PATH")

# OpenID Connect configuration
oidc_client_secrets_json = {
    "web": {
        "client_id": os.getenv("ROOM_OIDC_CLIENT_ID"),
        "client_secret": os.getenv("ROOM_OIDC_CLIENT_SECRET"),
        "auth_uri": os.getenv("ROOM_OIDC_AUTH_URL"),
        "token_uri": os.getenv("ROOM_OIDC_TOKEN_URL"),
        "userinfo_uri": os.getenv("ROOM_OIDC_USERINFO_URL"),
        "issuer": os.getenv("ROOM_OIDC_ISSUER"),
        "redirect_uris": [os.getenv("ROOM_OIDC_REDIRECT_URL")],
    }
}
oidc_logout_url = os.getenv("ROOM_OIDC_LOGOUT_URL")
oidc_overwrite_redirect_uri = os.getenv("ROOM_OIDC_REDIRECT_URL")