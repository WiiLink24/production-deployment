import os

# Primary config for cam-server
db_url = f"postgresql://{os.getenv('CAM_DB_USER')}:{os.getenv('CAM_DB_PASSWORD')}@postgres/{os.getenv('CAM_DB_DATABASE')}"
