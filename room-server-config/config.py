# Please ensure this file has its options synchronized with the example in room-server.
import os

# Primary config for room-server
db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@postgres/{os.getenv('POSTGRES_DB')}"

# This option should remain as-is without configuration if the default Compose definition is being used.
elasticsearch_url = "https://elastic:9200"
elasticsearch_user = os.getenv("ELASTIC_USER")
elasticsearch_pass = os.getenv("ELASTIC_PASS")

# Used as the base domain within first.bin.
root_domain = os.getenv("NGINX_BASE_DOMAIN")
# TODO: make toggleable once possible
root_https_enabled = False
# We assume we are being proxied with the default Compose definition.
root_separate_subdomain = True


# Used to secure the web panel.
underground_enabled = os.getenv("ROOM_UNDERGROUND_ENABLED") == "1"
secret_key = os.getenv("ROOM_SECRET_KEY")

# We use 2 servers, so we disable this here.
video_deletion_enabled = False

# We assume we are using localized time.
use_localized_time=False
maxmind_db_location = os.getenv("MAXMIND_DB_PATH")
