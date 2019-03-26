# K8S Example

This repo serves as a basic todo application in plain HTML and jQuery with a python backend running in flask, storing data on redis.

**NOTE**: This repo is still a work in progress so do not yet deploy on kubernetes. 

## Running

```
   cp env-example .env
   docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
   docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

This will run a basic docker cluster.

To run on k8s, deploy it using

```
   kubectl apply -f k8s
```
