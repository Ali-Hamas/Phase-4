# Spec: Local Kubernetes Deployment (Helm)

## Objective
Deploy the Todo Chatbot to a local Minikube cluster using Helm Charts.

## Architecture

## Chart Requirements
Create a Helm chart named `todo-app` with the following components:

### 1. Backend Deployment
- **Image**: todo-backend:v1
- **Replicas**: 1
- **Env Vars**: DATABASE_URL, OPENAI_API_KEY (use Secrets)
- **Service**: ClusterIP on port 8000

### 2. Frontend Deployment
- **Image**: todo-frontend:v1
- **Replicas**: 1
- **Env Vars**: NEXT_PUBLIC_API_URL pointing to the backend service
- **Service**: NodePort or LoadBalancer (for browser access)

### 3. ConfigMaps & Secrets
- Use a Secret for sensitive keys (API Keys, DB URL).
- Use ConfigMap for non-sensitive settings.

### 4. Database
- For this phase, continue connecting to the external Neon DB, OR deploy a local Postgres pod within the chart if preferred.