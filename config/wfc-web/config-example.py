db_url = ""
wfc_patches_db_url = ""

# Used to secure the web panel.
secret_key = ""

# Authentik API configuration
authentik_api_url = ""
authentik_service_account_token = ""

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
        "redirect_uris": "",
    }
}
oidc_logout_url = ""

# Moderator group UUID for access control
moderator_group_uuid = ""

# API URLs for WFC and Ban Info
wfc_stats_api = ""
wfc_groups_api = ""
ban_info_api = ""
