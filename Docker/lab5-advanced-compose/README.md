# Lab 5 – Advanced Docker Compose

Features:
- Scaling backend
- Load-balancing via Docker DNS
- Secrets via file mounts
- Healthchecks
- Dev overrides (live code editing)
- Postgres + Flask + Nginx full stack

## Commands

Build + start:
docker compose up --build -d

Scale backend:
docker compose up -d --scale backend=4

Test DNS load balancing:
docker exec -it $(docker compose ps -q frontend)
sh -c "apk add curl >/dev/null; for i in 1 2 3 4; do curl -s http://backend:5000/api/hello; echo; done"

Simulate backend crash:
docker exec -it <backend-container> pkill -9 python

Cleanup:
docker compose down --rmi local --volumes
