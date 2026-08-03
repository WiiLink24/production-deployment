FROM dockurr/dnsmasq:latest

COPY conf.d/*.conf /etc/dnsmasq.d
COPY --chmod=755 entrypoint.sh /usr/bin/wiilink-entrypoint.sh

ENTRYPOINT [ "/usr/bin/wiilink-entrypoint.sh" ]