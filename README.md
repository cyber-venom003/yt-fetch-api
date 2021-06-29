# YouTube-Fetch-API

## Objective
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Core Functionalities

- Server calls the YouTube API continuously in background (async) with some interval (here, 30 seconds) for fetching the latest videos for a predefined search query and stores the data of videos (specifically these fields - Video title, description, publishing datetime) in a database with proper indexes.

- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

- A basic search API to search the stored videos using their title and description.

- Dockerized project with different docker containers for server, Celery Worker and Beat, MySQL and Redis

- Scalable and Optimized

## Build Instructions

### Complete Build

To build all docker containers together, clone this repo, and run following command in CLI:

``` 
docker-compose up
```
This will build following docker containers and run them:

- Redis 
- MySQL
- Celery Worker
- Celery Beat
- FastAPI Web Server (uvicorn ASGI)

### Build Individual Containers

For building containers individually, this repo has individual dockerfiles and docker-compose for each service.

#### Build YouTube Fetch Queue Container

```
cd app 
```
```
docker-compose up
```

#### Build FastAPI Web Servcer Container

```
cd web_server
```
```
docker-compose up
```
### Run from source
To run application directly from source, follow following commands

MySQL
```
docker run -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 mysql
```
Redis
```
docker run -it --rm --name redis --net redis -p 6379:6379 redis:6.0-alpine
```
Run Celery Worker and Beat
```
celery -A worker.celery_worker worker -l info
```
```
celery -A worker.celery_worker beat -l info
```
Run FastAPI Web Server
```
cd ../web_server
```
```
uvicorn main:app --reload
```
