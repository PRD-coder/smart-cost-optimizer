# Smart Cost Optimizer for Kubernetes on AWS

## Project Overview

This project is an automated Kubernetes cost optimization system that monitors pod CPU usage using Prometheus and dynamically scales Kubernetes deployments to reduce infrastructure cost.


## Features

- Kubernetes deployment automation
- Prometheus monitoring integration
- Grafana dashboards
- Real-time CPU metric collection
- Automatic pod scaling using Python
- Cost optimization logic


## Tech Stack

- Kubernetes
- Docker
- Prometheus
- Grafana
- Python
- Minikube


## Architecture

Application Pods
↓
Prometheus collects metrics
↓
Python optimizer analyzes CPU usage
↓
Kubernetes deployment scales automatically


## Optimization Logic

If CPU usage is below threshold:
- Reduce replicas
- Save infrastructure resources

---

## Run Project

### Start Minikube

```bash
minikube start --driver=docker
```

### Deploy Application

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Run Optimizer

```bash
python optimizer.py
```

## Future Improvements

- AWS EKS deployment
- CI/CD pipeline using Jenkins
- Slack alerts
- Intelligent predictive scaling

## Author

Pranav Deshmukh
