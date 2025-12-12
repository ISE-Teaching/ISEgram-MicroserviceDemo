# ISEgram

A demo application to play around with deployment methods

> [!CAUTION]
> This is the gRPC branch, start with main!


## Process

In this [hands-on experience](https://cryptpad.fr/code/#/3/code/view/d2109a04be292d0ad22499c21afbb3c1/present/), we deploy the same services in different ways:

### 1. Create two services communicating with each other

  * Create multiple simple [flask](https://flask.palletsprojects.com/en/stable/quickstart/) services, with one calling the other.
  * Create a Python venv
  * Install dependencies
  * Run using Python

```
python3 main.py
```


### 2. Build the services using Docker

Create a Dockerfile, minding to install Python dependencies


```bash
docker build . -t cse-frontend
docker run -p 24001:24001 cse-frontend
```

### 3. Build and connect the services with Docker Compose

```bash
docker compose up --build
```


### 4. Create k8s manifests and deploy manually

**Start Minikube** (dashboard and tunnel run in the foregrund, so run in seperate terminals)

```bash
minikube start
minikube dashboard
minikube tunnel 
```

  * Deploy each service seperately to K8S, creating a service and a deployment 

### 5. Use skaffold

The *dev* command will make sure we run in the foreground, tear down resources when quitting skaffold, and automatically rebuild when the source code changes.

```
skaffold dev
```

### 6. Connect services with gRPC instead of REST

1. this has nothing todo with gRPC, but in this branch we use [uv](https://docs.astral.sh/uv/) as a python package manager 
2. the protobuf definition is in `/src/`
3. to compile the protobuf file to python code, we run `protoc` from the grpcio-tools in Python for each service:

```bash
cd src/frontend
uv run python -m grpc_tools.protoc --proto_path=.. --python_out=. --grpc_python_out=. ../posts.proto
```

3. This generates `posts_pb2.py` containing the classes / messages and `posts_pb2_grpc.py`, containing the server and client methods
4. following the [grpc tutorial](https://grpc.io/docs/languages/python/basics/), we now create a server in the posts service (instead of using flask) and the client ("stub") in the frontend service



### Advanced

  * Autoscaling
  * Add more services
  * Sidecars
  * Instrumentation
  * ...

**Run locust**
```
locust -H http://localhost:17000
```

