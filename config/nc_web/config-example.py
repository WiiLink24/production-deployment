db_url = ""

# Used to secure the web panel.
secret_key = ""
debug = False

# Used to secure communications to file generator
socket_secret = "please_change_thank_you"

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
