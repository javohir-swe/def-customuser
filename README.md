Here’s the updated and formatted version of your `README.md` file, with corrections and proper Markdown syntax:

```markdown
# Django Custom User API

A Django REST Framework project implementing custom user authentication with JWT tokens.

## Getting Started

Follow these steps to set up the project locally.

---

### Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose

---

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/javohir-swe/drf.git
   cd drf-customuser
   ```

2. Create an environment file:
   ```bash
   cp .env.example .env
   ```

3. Build and start Docker containers:
   ```bash
   docker-compose up --build
   ```

4. Create database migrations:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

5. Create a superuser account:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

---

### Access Points

After successful installation, you can access:

- **API Documentation**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Django Admin**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **API Endpoints**: [http://localhost:8000/api/](http://localhost:8000/api/)

---

### Database Configuration

The PostgreSQL database is accessible at:

- **Host**: `localhost`
- **Port**: `5434`

Default credentials are available in the `.env` file.

---

### API Features

- Custom User Authentication
- JWT Token Authentication
- Swagger Documentation
- RESTful API Endpoints
