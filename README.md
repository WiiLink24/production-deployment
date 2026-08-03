# production-deployment
An assortment of Compose definitions for production usage.

### Setup
1. Copy `.env.example` to `.env` and fill it out
2. Copy `config/eula.example.txt` to `config/eula.txt` and edit to your liking.
3. Within the `config` folder, copy each `config-example` and `.env.example` file and fill them out.

> [!TIP]
> Not using a Wireguard VPN? You will need to go through containers in the compose, replacing their `network-mode:` lines with standard `networks:` lines. You will also need to replace instances of `wireguard_client` in the nginx templates with the container name (e.g. `demae_dominos`)

### Starting your server
**Running a specific service** (i.e. News Channel) - `docker compose up -d news_channel`

**Running the whole stack** - `docker compose up -d`
