#!/bin/bash

rm -rf htmlcov

docker network disconnect tm_network jupyter
docker network disconnect tm_network fastapi
docker network disconnect tm_network postgres
docker network disconnect tm_network unittest
docker network rm tm_network
docker stop postgres
docker stop fastapi
docker stop jupyter
docker stop unittest
docker remove postgres
docker remove fastapi
docker remove jupyter
docker remove unittest
docker volume rm $(docker volume ls -q)
# docker rmi $(docker images -q)
