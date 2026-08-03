# Please ensure this file has its options synchronized with the example in room-server.
import os

# Primary config for room-server
db_url = ""

# Used as the base domain within first.bin.
root_domain = os.getenv("ROOM_BASE_DOMAIN")
# TODO: make toggleable once possible
root_https_enabled = False
# We assume we are being proxied with the default Compose definition.
root_separate_subdomain = True


# Used to secure the web panel.
secret_key = ""

# Sentry configuration for error logging.
use_sentry = True
sentry_dsn = ""

use_s3 = False
r2_account_id = ""
r2_bucket_name = ""
s3_connection_url = ""
s3_access_key_id = ""
s3_secret_access_key = ""

url1_cdn_url = ""
url3_cdn_url = ""

ds_rsa_key_path = ""

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

community_photos_dir = ""