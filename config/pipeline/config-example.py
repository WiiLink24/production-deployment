# If you're adding a new config option, please update WiiLink24/production-deployment's
# copy of config.py to match the new options once committed to master.

# OpenID Connect configuration
oidc_redirect_uri = "http://localhost:8080/authorize"
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