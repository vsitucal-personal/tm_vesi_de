#!/bin/bash

# Check if DB_PASS is provided as an argument
if [ -z "$1" ]; then
  echo "Error: DB_PASS is required."
  echo "Usage: ./docker_setup.sh <DB_PASS>"
  exit 1
fi

DB_PASS=$1

# Create the network
docker network create tm_network

# Run the PostgreSQL container
docker run -d --name postgres --network tm_network postgres

# Run the unittest container
docker run -d --name unittest --network tm_network -p 8000:8000 unittest

# Run the FastAPI container
docker run -d --name fastapi --network tm_network -p 80:80 \
  -e DB_HOST=postgres \
  -e DB_PORT=5432 \
  -e DB_NAME=postgres \
  -e DB_USER=postgres \
  -e DB_PASS=$DB_PASS \
  fastapi

# Run the Jupyter container
docker run -d --name jupyter --network tm_network -p 4040:4040 -p 8888:8888 \
  -e DB_HOST=postgres \
  -e DB_PORT=5432 \
  -e DB_NAME=postgres \
  -e DB_USER=postgres \
  -e DB_PASS=$DB_PASS \
  jupyter

echo "Containers have been started successfully with DB_PASS=$DB_PASS"
