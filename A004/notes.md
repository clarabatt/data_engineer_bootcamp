# Docker and SQL

## Docker

### Build a image

`docker build -t [IMG NAME] [PATH]`

Example:

`docker build -t web_apache .`

### Remove an image

`docker image rm [OPTIONS] IMAGE`

### Show image list

`docker image ls`

### Run a image

`docker run -d -p [PORT] [IMAGE]`

Example:

`docker run -d -p 80:80 web_apache`

### Actived containers

`docker ps`

### Stop container

`docker stop [ID]`

## Compose

### Up

`docker-compose up -d [SERVICE]`

`docker-compose down`

`docker-compose ps`
