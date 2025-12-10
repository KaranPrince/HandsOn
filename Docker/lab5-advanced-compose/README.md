Lab 5 – Advanced Docker Compose (with Volumes lab)

Start:
  docker compose up --build -d

Status:
  docker compose ps
  docker compose logs -f backend

Test:
  http://127.0.0.1:8082  # open in browser

Scale backend:
  docker compose up -d --scale backend=4 --no-recreate

DNS test (from frontend container):
  docker exec -it $(docker compose ps -q frontend) /bin/sh -c "apk add --no-cache curl >/dev/null 2>&1 || true; for i in 1 2 3 4; do curl -sS http://backend:5000/api/hello; echo; done"

Backup volume:
  docker run --rm -v lab5-advanced-compose_dbdata:/volume -v ${PWD}:/backup alpine sh -c "cd /volume && tar -czf /backup/dbdata-backup.tar ."

Restore volume:
  docker compose down
  docker volume rm lab5-advanced-compose_dbdata
  docker volume create --name lab5-advanced-compose_dbdata
  docker run --rm -v lab5-advanced-compose_dbdata:/volume -v ${PWD}:/backup alpine sh -c "cd /volume && tar -xzf /backup/dbdata-backup.tar"
  docker compose up -d

Cleanup:
  docker compose down --rmi local --volumes
