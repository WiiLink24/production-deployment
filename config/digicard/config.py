import os

# Primary config for Digicard
db_url = f"postgresql://{os.getenv('CAM_DB_USER')}:{os.getenv('CAM_DB_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('CAM_DB_DATABASE')}"

# Used to secure the website.
secret_key = os.getenv("DIGICARD_SECRET_KEY")

# Used for Oauth2 with Discord.
discord_client_id = os.getenv("DIGICARD_CLIENT_ID")
discord_client_secret = os.getenv("DIGICARD_CLIENT_SECRET")
# Default to https://<domain>/callback.
discord_redirect_uri = f"https://{os.getenv('DIGICARD_DOMAIN')}/callback"
