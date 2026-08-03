import os

# Primary config for Digicard
db_url = ""

# Used to secure the website.
secret_key = ""

# Used for Oauth2 with Discord.
discord_client_id = ""
discord_client_secret = ""
# Default to https://<domain>/callback.
discord_redirect_uri = f"https://{os.getenv('DIGICARD_DOMAIN')}/callback"
