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
underground_enabled = os.getenv("ROOM_UNDERGROUND_ENABLED") == "1"
secret_key = os.getenv("ROOM_SECRET_KEY")

video_deletion_enabled = True

# We assume we are using localized time.
use_localized_time = True
maxmind_db_location = os.getenv("MAXMIND_DB_PATH")

# Sentry configuration for error logging.
use_sentry = True
sentry_dsn = os.getenv("ROOM_SENTRY_DSN")
