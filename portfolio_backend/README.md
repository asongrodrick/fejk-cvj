# Portfolio Backend (Django) - Setup Instructions

## Overview
This package contains:
- A Django project `portfolio_backend`
- An app `portfolio` with models for `Project` and `ContactMessage`
- Admin configuration for managing projects and contact messages
- API endpoints:
  - `GET /api/projects/` — returns JSON list of projects
  - `POST /contact/` — accepts contact form submissions (and also a form at /contact/)

## Prerequisites
- Python 3.10+ (or recent 3.x)
- pip
- MySQL or MariaDB server
- (Optional) virtualenv

## Quick setup
1. Create Python virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # linux / mac
   venv\Scripts\activate    # windows
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a MySQL database and user (example commands):
   ```sql
   -- Connect as root or admin user
   CREATE DATABASE portfolio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'portfolio_user'@'localhost' IDENTIFIED BY 'change_me';
   GRANT ALL PRIVILEGES ON portfolio_db.* TO 'portfolio_user'@'localhost';
   FLUSH PRIVILEGES;
   ```
   Replace `change_me` with a secure password and update `portfolio_backend/portfolio_backend/settings.py` accordingly.

4. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Collect static files (for production) and run server locally for testing:
   ```bash
   python manage.py collectstatic
   python manage.py runserver 0.0.0.0:8000
   ```

## Notes on frontend
- Your provided frontend files are included in the `frontend/` folder.
- You can either serve those static files separately (e.g., with nginx) or integrate them into Django's `templates/` and `static/` folders.

## Adding / Editing Projects
- Use the Django admin at `/admin/` to add projects, or implement additional API endpoints for authenticated CRUD operations.

## Security & Production
- Set `DEBUG = False` in production and configure `ALLOWED_HOSTS`.
- Use a secure SECRET_KEY and configure HTTPS, allowed hosts, and proper static file hosting.

## Contact
For help customizing the backend further, reply with what you'd like changed.
