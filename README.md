# production-deployment
In-use compose file for running WiiLink services in production.

### Setup
1. Copy `.env.example` to `.env` and fill it out
2. Copy `config/eula.example.txt` to `config/eula.txt` and edit to your liking.
3. Within the `config` folder, copy each `config-example` and `.env.example` file and fill them out.

> [!TIP]
> Not using a Wireguard VPN? You will need to go through containers in the compose, replacing their `network-mode:` lines with standard `networks:` lines. You will also need to replace instances of `wireguard_client` in the nginx templates with the container name (e.g. `demae_dominos`)

> [!WARNING]
> If you aren't running all services, you will need to remove the services you aren't running from the nginx templates folder. Otherwise, nginx will get stuck in a loop and fail to start.

> [!IMPORTANT]
> For all containers to be able to read and write data correctly, you will need to give your host user's group read-write permissions to the directories where you store data, as well as setting the SGID:
> ```bash
> chmod g+rwxs ./data
> ```

### Starting your server
**Running a specific service** (i.e. News Channel) - `docker compose up -d news_channel`

**Running the whole stack** - `docker compose up -d`
