from kubernetes import client, config
import requests

# Load kube config
config.load_kube_config()

apps_v1 = client.AppsV1Api()

DEPLOYMENT_NAME = "smart-cost-app"
NAMESPACE = "default"

# Prometheus API
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

# Query smart-cost-app CPU usage
query = 'container_cpu_usage_seconds_total{namespace="default",pod=~"smart-cost-app.*"}'

response = requests.get(
    PROMETHEUS_URL,
    params={"query": query}
)

data = response.json()

results = data["data"]["result"]

# Calculate total CPU usage
total_cpu = 0

for item in results:
    value = float(item["value"][1])
    total_cpu += value

print(f"Total CPU Usage: {total_cpu}")

# Optimization logic
deployment = apps_v1.read_namespaced_deployment(
    DEPLOYMENT_NAME,
    NAMESPACE
)

current_replicas = deployment.spec.replicas

print(f"Current Replicas: {current_replicas}")

# If CPU usage low → scale down
if total_cpu < 1:

    if current_replicas > 1:

        deployment.spec.replicas = current_replicas - 1

        apps_v1.patch_namespaced_deployment(
            DEPLOYMENT_NAME,
            NAMESPACE,
            deployment
        )

        print("Optimization Applied: Scaled Down")

    else:
        print("Minimum replicas reached")

else:
    print("CPU usage high — no scaling")