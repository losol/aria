# Update Docker image

This document describes how to update the Docker image for the [Docker image](https://hub.docker.com/r/losolio/aria)

## Build the image

```bash
docker build . --tag losolio/aria
```

## Push the image

After logging in with `docker login`, push the image to the Docker Hub:

```bash
docker push aria:latest
```
