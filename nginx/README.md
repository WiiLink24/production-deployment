# nginx
The `static` folder holds static HTML mounted to `/var/www/static` in the container, while `templates` holds nginx config templates. 

> [!TIP]
> Not running all services? You will need to remove the config files from the `templates` directory for the services you are not running, otherwise nginx will fail to start.
