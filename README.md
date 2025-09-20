# Personal Portfolio Website

This project is a personal portfolio website designed to showcase your work, skills, and achievements. It features a clean, professional, and responsive design, an administrative area for managing projects without code changes, and is built with a modern tech stack (React, FastAPI, PostgreSQL).

## Features:

*   **Homepage:** Introduces you with a clean and professional design.
*   **About Me Page:** Details your background, experience, and achievements.
*   **Projects Page:** Displays your past work with images, descriptions, and links.
*   **Contact Page:** A simple form for visitors to get in touch.
*   **Private Admin Area:** Secure section to add, edit, and remove projects without code modifications.

## Tech Stack:

*   **Frontend:** React
*   **Backend:** FastAPI (Python)
*   **Database:** PostgreSQL
*   **Containerization:** Docker, Docker Compose

## Project Structure:

```
/
├── backend/                     # FastAPI app
│   ├── app/
│   │   ├── main.py              # Entry point
│   │   ├── core/                # Config, database, security
│   │   ├── models/              # SQLAlchemy models
│   │   ├── schemas/             # Pydantic schemas
│   │   ├── services/            # Business logic
│   │   ├── routers/             # API routes
│   │   ├── utils/               # Utilities (security, logger, etc.)
│   │   ├── dependencies.py      # Common dependencies
│   ├── tests/                   # Pytest cases
│   ├── alembic/                 # Database migrations
│   ├── requirements.txt         # Backend dependencies
│   ├── .env                     # Environment variables
│
├── frontend/                    # React app
│   ├── src/
│   │   ├── components/          # Reusable UI components
│   │   ├── pages/               # Page-level components
│   │   ├── services/            # API calls (axios/fetch)
│   │   ├── hooks/               # Custom React hooks
│   │   ├── context/             # Global context/state
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   ├── package.json             # Frontend dependencies
│
├── docker-compose.yml           # Services definition (FastAPI + PostgreSQL + React)
├── Dockerfile.backend           # Backend container
├── Dockerfile.frontend          # Frontend container
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
```

## Getting Started (Local Development):

**Prerequisites:**

*   Docker and Docker Compose installed.
*   Git installed.

**Steps:**

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd personal-portfolio
    ```

2.  **Environment Variables:**

    *   Create a `.env` file in the `backend/` directory. (Content will be added later)
    *   Create a `.env` file in the `frontend/` directory if needed. (Content will be added later)

3.  **Build and Run with Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    This command will:
    *   Build the backend and frontend Docker images.
    *   Start the PostgreSQL, FastAPI, and React services.

4.  **Access the Application:**

    *   Frontend (React): `http://localhost:3000` (or as configured in `docker-compose.yml`)
    *   Backend (FastAPI): `http://localhost:8000` (or as configured in `docker-compose.yml`)
    *   FastAPI Docs: `http://localhost:8000/docs`

## Deployment (Coming Soon)

Detailed instructions for deploying the application to a production environment will be provided in a later update. This will cover options such as Vercel (for frontend), Render/Heroku (for backend), or a custom VPS with Nginx.
