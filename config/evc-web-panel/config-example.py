# Database so we can keep script size low
db_url = ""

# Used to secure the web panel.
secret_key = ""

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
