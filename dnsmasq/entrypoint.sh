#!/usr/bin/env bash

# Set HOST_IP to actual value in config files
sed -i 's/HOST_IP/'$HOST_IP'/' /etc/dnsmasq.d/*

# Standard entrypoint command
/usr/bin/dnsmasq.sh