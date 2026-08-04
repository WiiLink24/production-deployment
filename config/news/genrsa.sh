#!/usr/bin/env bash

if ! type -P openssl >/dev/null 2>&1 ; then
    echo "OpenSSL is not available in PATH! Install OpenSSL to run this script"
    exit 1
else
    openssl genrsa -traditional -out Private.pem
fi