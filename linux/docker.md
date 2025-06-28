# Docker commands
docker pull <image name> (look from dockerhub by default)

docker build . (look for dockerfile in relative path and build image)
docker build -t <repo name> . (-t = tag, build with a name)
docker images (see list of images)

docker run -d <imageID> (detached mode)
docker run -p 5000:8080 dockerID (-p = port, 5000 local, 8080 container)
docker run --name <containerName> (run a container with input name)

docker ps (list of running containers)
docker ps -a (-a = all, all containers included not running)

docker stop <containerID>
docker start <containerID>

docker rm <containerID> (remove container)
docker rmi <imageID> (remove image)

docker compose up -d (run in background)
docker compose down

# Postgres
docker exec -it <container ID> psql -U <user, server name> (psql into database)