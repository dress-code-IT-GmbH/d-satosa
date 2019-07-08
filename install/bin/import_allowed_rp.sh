#!/bin/bash

# import allowed relying parties from rpmgr container

cp /opt/satosa_rpmgr/export/custom_routing_DecideIfRequesterIsAllowed.yaml \
   /opt/etc/satosa/plugins/microservices/custom_routing_DecideIfRequesterIsAllowed.yaml