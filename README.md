# ISEgram

## GRPC

0. this has nothing todo with gRPC, but in this branch we use [uv](https://docs.astral.sh/uv/) as a python package manager 
1. the protobuf definition is in `/src/`
2. to compile the protobuf file to python code, we run `protoc` from the grpcio-tools in Python for each service:

```bash
cd src/frontend
uv run python -m grpc_tools.protoc --proto_path=.. --python_out=. --grpc_python_out=. ../posts.proto
```

3. This generates `posts_pb2.py` containing the classes / messages and `posts_pb2_grpc.py`, containing the server and client methods
4. following the [grpc tutorial](https://grpc.io/docs/languages/python/basics/), we now create a server in the posts service (instead of using flask) and the client ("stub") in the frontend service

## Process

### 1. Create two services communicating with each other
### 2. Build the services using Docker
### 3. Build and connect the services with Docker Compose
### 4. Create k8s manifests and deploy (with skaffold)


**Start Minikube**
dashboard and tunnel run in the foregrund, so run in seperate terminals

```bash
minikube start
minikube dashboard
minikube tunnel 
```

**Deploy with skaffold**
The dev command will make sure we run in the foreground, tear down resources when quitting skaffold, and automatically rebuild when the source code changes.

```bash
skaffold dev
```

**Run locust**
```
locust -H http://localhost:17000
```

### 5. Scale to multiple replicas
### Advanced

  * Autoscaling
  * Add more services
  * Sidecars
  * Instrumentation

## GRPC

 * https://grpc.io/docs/what-is-grpc/introduction/
 * https://grpc.io/docs/languages/python/basics/

```
python3.10 -m grpc_tools.protoc --proto_path=.. --python_out=. --grpc_python_out=. ../posts.proto
```