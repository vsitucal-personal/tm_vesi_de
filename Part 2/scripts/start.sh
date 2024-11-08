docker network create tm_network
docker run -d --name postgres --network tm_network postgres
docker run -d --name unittest --network tm_network unittest
docker run -d --name fastapi --network tm_network -p 80:80 \
  -e DB_HOST=postgres \
  -e DB_PORT=5432 \
  -e DB_NAME=postgres \
  -e DB_USER=postgres \
  -e DB_PASS=1234 \
  fastapi
docker run -d --name jupyter --network tm_network -p 4040:4040 -p 8888:8888 \
  -e DB_HOST=postgres \
  -e DB_PORT=5432 \
  -e DB_NAME=postgres \
  -e DB_USER=postgres \
  -e DB_PASS=1234 \
  jupyter