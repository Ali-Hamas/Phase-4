# Spec: Docker Containerization

## Objective
Containerize the Frontend (Next.js) and Backend (FastAPI) applications for the Todo Chatbot.

## Requirements
### Backend Container
- Base Image: Python 3.13-slim
- Working Directory: /app
- Dependencies: Install from `pyproject.toml` or `requirements.txt`
- Expose Port: 8000
- Command: Run uvicorn server

### Frontend Container
- Base Image: Node 20-alpine
- Build Step: Run `npm run build`
- Expose Port: 3000
- Command: Start Next.js app

### Docker Compose (for local testing)
- Define services for `frontend`, `backend`, and `db` (Postgres/Neon proxy).
- Ensure environment variables are passed correctly.