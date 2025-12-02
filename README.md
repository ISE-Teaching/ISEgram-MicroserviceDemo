# ISEgram


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

