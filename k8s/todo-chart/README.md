# Todo App Helm Chart

This Helm chart deploys the Todo Chatbot application to a Kubernetes cluster.

## Chart Structure

```
todo-app/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── _helpers.tpl
    ├── deployment-backend.yaml
    ├── deployment-frontend.yaml
    ├── service-backend.yaml
    ├── service-frontend.yaml
    ├── secrets.yaml
    ├── configmap.yaml
    └── database.yaml
```

## Configuration

The following table lists the configurable parameters of the todo-app chart and their default values.

### Backend Configuration
| Parameter | Description | Default |
|-----------|-------------|---------|
| `backend.replicaCount` | Number of backend pods | `1` |
| `backend.image.repository` | Backend image repository | `todo-backend` |
| `backend.image.tag` | Backend image tag | `v1` |
| `backend.image.pullPolicy` | Backend image pull policy | `IfNotPresent` |
| `backend.service.type` | Backend service type | `ClusterIP` |
| `backend.service.port` | Backend service port | `8000` |

### Frontend Configuration
| Parameter | Description | Default |
|-----------|-------------|---------|
| `frontend.replicaCount` | Number of frontend pods | `1` |
| `frontend.image.repository` | Frontend image repository | `todo-frontend` |
| `frontend.image.tag` | Frontend image tag | `v1` |
| `frontend.image.pullPolicy` | Frontend image pull policy | `IfNotPresent` |
| `frontend.service.type` | Frontend service type | `NodePort` |
| `frontend.service.port` | Frontend service port | `80` |

### Secrets Configuration
| Parameter | Description | Default |
|-----------|-------------|---------|
| `secrets.create` | Whether to create secrets | `true` |

### Database Configuration
| Parameter | Description | Default |
|-----------|-------------|---------|
| `database.deployLocal` | Deploy local Postgres instance | `false` |

## Installation

To install the chart with the release name `todo-app-release`:

```bash
helm install todo-app-release k8s/todo-chart
```

To install with custom values:

```bash
helm install todo-app-release k8s/todo-chart --set secrets.databaseUrl="your-db-url" --set secrets.openaiApiKey="your-api-key"
```

## Uninstallation

To uninstall/delete the `todo-app-release` deployment:

```bash
helm delete todo-app-release
```

## Values File Example

Create a `custom-values.yaml` file to override default values:

```yaml
backend:
  replicaCount: 2
  service:
    port: 8080

frontend:
  replicaCount: 2
  service:
    type: LoadBalancer

secrets:
  create: true
  databaseUrl: "your-database-url-here"
  openaiApiKey: "your-openai-api-key-here"

database:
  deployLocal: true
```

Then install with:

```bash
helm install todo-app-release k8s/todo-chart -f custom-values.yaml
```