# production-deployment
An assortment of Compose definitions for production usage.

### Files
(To be detirmined, eventually i will update this with a simple README that reflects the new setup)

```
docker-compose.yml
```
This file specifies all of the docker containers that run in a prod environment.

```
prod.wiilink24.com.conf
```
This file contains the NGINX configuration used in a prod environment.

### Setup
1. Copy `.env.example` to `.env` and make edits accordingly for the PostgreSQL database's credentials, base domain, and other items.
2. Ensure assets are present within the `assets` folder for usage with `room-server`.
3. Ensure [room-server](https://github.com/WiiLink24/room-server), [cam-server](https://github.com/WiiLink24/cam-server) and [food-server](https://github.com/WiiLink24/food-server) are cloned within this folder.
4. Copy `config/eula.example.txt` to `config/eula.txt` and edit to your liking.
5. Within the `config` folder, read each README for per-server configuration.
6. `docker-compose up` will bring your server up on `<release_type>.<base_domain>`!

For example, if `<base_domain>` is defined as `example.com` and `<release_type>` is "prod", your server will be available on `prod.example.com`.
