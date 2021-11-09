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

## SQL

`SELECT DISTINCT`
> avoid in big data bases

## Interaction with DB using Python

1. Install SQLAlchemy
`pip install SQLAlchemy`

2. Install psycopg
`pip install psycopg`

Creating engine:

```python
engine = create_engine(
    'postgresql+psycopg2://user:password@hostname/database_name'
)
```
