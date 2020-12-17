# Please ensure this file has its options synchronized with the example in room-server.
import os

db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@postgres/{os.getenv('POSTGRES_DB')}"
secret_key = os.getenv("ROOM_SECRET_KEY")
underground_enabled = os.getenv("ROOM_UNDERGROUND_ENABLED") == "1"
# This option should remain as-is without configuration if the default Compose definition is being used.
elasticsearch_url = "elastic:9200"
