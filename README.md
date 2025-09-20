# Personal Portfolio Website

This project is a personal portfolio website designed to showcase your work and skills. It features a modern, responsive design and includes an admin area for easy management of projects.

## Features

*   **Homepage:** A clean and professional introduction.
*   **About Me Page:** Detailed background, experience, and achievements.
*   **Projects Page:** Display your work with images, descriptions, and links.
*   **Contact Page:** A simple form for visitors to send messages.
*   **Admin Area:** A private section to add, edit, or remove projects without coding.
*   **Fast & Secure:** Optimized for performance and security.
*   **Responsive Design:** Works well on both mobile and desktop devices.

## Technologies Used

*   **Frontend:** React.js
*   **Backend:** FastAPI (Python)
*   **Database:** PostgreSQL
*   **Containerization:** Docker, Docker Compose

## Project Structure

```
.gitignore
README.md
docker-compose.yml
Dockerfile.backend
Dockerfile.frontend

backend/
├── alembic/
├── app/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── dependencies.py
│   └── main.py
├── tests/
├── .env
└── requirements.txt

frontend/
├── public/
├── src/
│   ├── components/
│   ├── context/
│   ├── hooks/
│   ├── pages/
│   ├── services/
│   ├── App.js
│   └── index.js
└── package.json
```

## Setup and Installation

Follow these steps to get your personal portfolio website up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   [Docker Desktop](https://www.docker.com/products/docker-desktop)
*   [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-portfolio.git
cd your-portfolio
```

### 2. Configure Environment Variables

Create a `.env` file in the `backend/` directory with the following content:

```env
DATABASE_URL=postgresql://user:password@db:5432/portfolio_db
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

*   `DATABASE_URL`: Connection string for your PostgreSQL database.
*   `SECRET_KEY`: A strong secret key for JWT authentication. You can generate one using `openssl rand -hex 32`.
*   `ALGORITHM`: The algorithm used for JWT signing (e.g., HS256).
*   `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes.

### 3. Build and Run with Docker Compose

Navigate to the root directory of the project (where `docker-compose.yml` is located) and run:

```bash
docker-compose build
docker-compose up
```

This will build the Docker images for your frontend and backend, and then start the services. It might take a few minutes for the first build.

### 4. Database Migrations

Once the services are running, you'll need to apply database migrations. Connect to the backend container:

```bash
docker-compose exec backend alembic upgrade head
```

This command will apply all pending database migrations.

### 5. Access the Application

*   **Frontend:** Open your web browser and go to `http://localhost:3000`
*   **Backend API (Swagger UI):** `http://localhost:8000/docs`

## Admin Area

To access the admin area, you will need to register an admin user through the API (e.g., via Swagger UI) and then log in. The frontend admin routes will be protected.

## Deployment

For deployment to a production server, consider using a cloud provider like AWS, Google Cloud, or DigitalOcean. You would typically use a reverse proxy like Nginx, manage environment variables securely, and set up a robust CI/CD pipeline.

## Contributing

Feel free to fork the repository and contribute! Please open an issue or pull request for any changes or improvements.

## License

This project is open source and available under the [MIT License](LICENSE).