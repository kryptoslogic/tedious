#!/bin/sh

openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -out certificate.pem
