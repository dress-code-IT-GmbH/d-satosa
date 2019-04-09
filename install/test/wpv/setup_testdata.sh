#!/bin/bash

cp -pr /opt/test/wpv/* $DATA_DIR
chmod 600 $DATA_DIR/pki/*key.pem
chown +x /opt/test/wpv/*.sh