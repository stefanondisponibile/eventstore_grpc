#!/bin/bash

# https://developers.eventstore.com/server/v21.10/installation.html#run-with-docker

docker run --name esdb-single-node -d -p 2113:2113 -p 1113:1113 \
  eventstore/eventstore:latest --insecure --run-projections=All
