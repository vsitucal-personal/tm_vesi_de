#!/bin/bash

# Check if DB_PASS is provided as an argument
if [ -z "$1" ]; then
  echo "Error: DB_PASS is required."
  echo "Usage: ./docker_build.sh <DB_PASS>"
  exit 1
fi

# Assign the first argument to DB_PASS
DB_PASS=$1

# Build the postgres image
docker build --build-arg DB_PASS=$DB_PASS -t postgres -f "Part 2/scripts/postgres" .

# Build the fastapi image
docker build -t fastapi -f "Part 2/scripts/fastapi" .

# Build the unittest image
docker build -t unittest -f "Part 2/scripts/unittest" .

# Build the jupyter image
docker build --build-arg jup_pass=$DB_PASS --build-arg jup_token="" \
  -t jupyter -f "Part 2/scripts/jupyter" .

echo "Docker images have been built successfully with pass=$DB_PASS"
