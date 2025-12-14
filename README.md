# Todo Chatbot Application

A full-stack application with a Next.js frontend and FastAPI backend for managing todos with chatbot-like functionality.

## Prerequisites

- Docker and Docker Compose
- Node.js (for local development without Docker)
- Python 3.13+ (for local development without Docker)

## Running with Docker Compose (Recommended)

1. Clone the repository and navigate to the project directory:
   ```bash
   cd Phase_4
   ```

2. Build and start the services:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Backend API Docs: http://localhost:8000/docs

## Running Locally (Without Docker)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Start the backend server:
   ```bash
   poetry run python -m app.main
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set environment variable for API URL:
   ```bash
   # On Windows (Command Prompt)
   set NEXT_PUBLIC_API_URL=http://localhost:8000

   # On Windows (PowerShell)
   $env:NEXT_PUBLIC_API_URL="http://localhost:8000"

   # On macOS/Linux
   export NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

5. Access the application at http://localhost:3000

## Features

- Add, edit, and delete todos
- Mark todos as completed
- Clear all todos
- Responsive UI design
- API endpoints for all todo operations

## API Endpoints

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `PUT /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a specific todo
- `DELETE /todos` - Delete all todos
- `GET /` - Health check endpoint

## Project Structure

```
Phase_4/
├── backend/              # FastAPI backend
│   ├── app/
│   │   └── main.py      # Main application file
│   ├── pyproject.toml   # Python dependencies
│   └── Dockerfile
├── frontend/             # Next.js frontend
│   ├── src/
│   │   └── pages/
│   │       └── index.js # Main page
│   ├── package.json     # Node.js dependencies
│   ├── next.config.js   # Next.js configuration
│   └── Dockerfile
├── docker-compose.yml    # Docker configuration
└── k8s/                 # Kubernetes configurations
```

## Troubleshooting

- If the frontend can't connect to the backend, ensure that the `NEXT_PUBLIC_API_URL` environment variable is set correctly
- If Docker build fails, try clearing Docker cache: `docker system prune -a`
- Make sure ports 3000 and 8000 are available on your system