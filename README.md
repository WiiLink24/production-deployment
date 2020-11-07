# production-deployment
An assortment of Compose definitions for production usage.

### Setup
1. Copy `.env.example` to `.env` and make edits accordingly for the PostgreSQL database's credentials, base domain, and other items.
2. Ensure assets are present within the `assets` folder.
3. `docker-compose up` will bring your server up on `<release_type>.<base_domain>`!

For example, if `<base_domain>` is defined as `example.com` and `<release_type>` is "prod", your server will be available on `prod.example.com`.