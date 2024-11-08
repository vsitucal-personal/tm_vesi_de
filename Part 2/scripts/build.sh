docker build -t postgres -f scripts/postgres .
docker build -t fastapi -f scripts/fastapi .
docker build -t jupyter -f scripts/jupyter .
docker build -t unittest -f scripts/unittest .