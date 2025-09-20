# Personal Portfolio Website

This project is a personal portfolio website built with React, FastAPI, and PostgreSQL. It features a modern, responsive design and a private admin area for managing projects.

## Features

*   **Homepage**: Introduction to the user.
*   **About Me Page**: Details about the user's background, experience, and achievements.
*   **Projects Page**: Displays work with images, descriptions, and external links.
*   **Contact Page**: A form for visitors to send messages.
*   **Private Admin Area**: Backend interface to add, edit, or remove project entries.

## Technologies Used

*   **Frontend**: React.js
*   **Backend**: FastAPI (Python)
*   **Database**: PostgreSQL
*   **Containerization**: Docker, Docker Compose

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Docker and Docker Compose installed.

### Installation

1.  **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd personal-portfolio
    ```

2.  **Set up environment variables**:

    Create a `.env` file in the `backend/` directory based on `backend/.env.example` (will be created later) and fill in the necessary database credentials and secret keys.

3.  **Build and run the Docker containers**:

    ```bash
    docker-compose up --build
    ```

    This command will:
    *   Build the backend and frontend Docker images.
    *   Start the PostgreSQL database container.
    *   Run the FastAPI backend on `http://localhost:8000`.
    *   Run the React frontend on `http://localhost:3000`.

### Accessing the Application

*   **Frontend**: `http://localhost:3000`
*   **Backend API**: `http://localhost:8000`
*   **Backend API Documentation (Swagger UI)**: `http://localhost:8000/docs`
*   **Backend API Alternative Documentation (Redoc)**: `http://localhost:8000/redoc`

## Project Structure

```
.gitignore
README.md
docker-compose.yml
Dockerfile.backend
Dockerfile.frontend

backend/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   └── project.py
│   ├── schemas/
│   │   └── project.py
│   ├── services/
│   │   └── project.py
│   ├── routers/
│   │   └── project.py
│   ├── utils/
│   │   └── security.py
│   └── dependencies.py
├── tests/
│   └── test_main.py
├── alembic/
│   └── env.py
├── requirements.txt
└── .env

frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   ├── context/
│   ├── App.js
│   └── index.js
└── package.json
```

## Deployment

Deployment instructions will be added here later.

## Contact

For any questions or suggestions, please contact [Your Name/Email].