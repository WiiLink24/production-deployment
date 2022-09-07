import os

db_url = f"postgresql://{os.getenv('DOMINOS_DB_USER')}:{os.getenv('DOMINOS_DB_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('DOMINOS_DB_DATABASE')}"

# Google Maps API key for Geocoder
google_api_key = os.getenv("DOMINOS_GOOGLE_MAPS_API_KEY")
