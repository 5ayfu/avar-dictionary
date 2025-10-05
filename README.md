# Avar Dictionary

Avar Dictionary is an open source project that collects and publishes Avar language resources. The repository contains a web application and REST API built with Django and Django REST Framework. It includes three major components:

- **Dictionary** – words with translations, usage examples and synonyms
- **Phrasebook** – practical phrases grouped by topic with transliteration
- **Grammar articles** – short explanations of grammar and language features

The goal is to provide an easily accessible reference for learners and researchers while offering an API that can power other software. All data is openly licensed so that search engines and language models can index and reuse these materials.

## Features

- Full text search with filters by language and part of speech
- Detailed word pages with translations, examples and synonyms
- Quick translation endpoint to convert words between languages
- Phrasebook pages for everyday expressions
- Grammar articles organized by topic
- Admin interface with import/export through `django-import-export`
- Swagger/OpenAPI documentation available at `/api/docs/`

## Quick start with Docker

1. Copy the example environment file and adjust the values if needed:
   ```bash
   cp .env.example .env
   ```
2. Build the containers and start the stack:
   ```bash
   docker compose up --build
   ```

The Docker configuration uses PostgreSQL by default. The application will be available at `http://localhost:8000/` once the migrations finish.

## Local installation

1. Install Python 3.12 and create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Repository structure

- `api/` – Django project configuration
- `dictionary/` – models and views for dictionary entries
- `phrasebook/` – models and views for the phrasebook
- `grammar/` – models and views for grammar articles
- `website/` – templates and static files
- `docker-compose.yml` and `Dockerfile` – container setup

## Example API requests

- List words: `GET /api/dictionary/words/`
- Search a word: `GET /api/dictionary/search/?q=word`
- Quick translation: `GET /api/dictionary/translate/?word=hello&from=en&to=av`
- Phrasebook entries: `GET /api/phrasebook/phrases/`
- Grammar articles: `GET /api/grammar/articles/`

A complete list of endpoints is available through Swagger UI (`/api/docs/`).

## Serving static files with Nginx

In production you will usually proxy requests through Nginx (or a similar web server) while it serves the collected static assets directly from disk or object storage. This project supports both approaches:

- **Whitenoise** – enabled by default and useful for simple deployments where Gunicorn can serve static assets itself. Set `DJANGO_USE_WHITENOISE=False` in the environment to disable it.
- **External web server** – when Whitenoise is disabled run `python manage.py collectstatic` (the provided Docker entrypoint already does this) and point Nginx at the resulting `staticfiles` directory.

The repository includes a sample configuration at `docker/nginx/default.conf`. Copy it to your server (for example `/etc/nginx/conf.d/avar.conf`), adjust the `server_name` and update the upstream host if Gunicorn listens on another address or port. Make sure the `alias` path matches the directory where you publish the collected static files, e.g. `/var/www/avar/static/`.

```nginx
location /static/ {
    alias /var/www/avar/static/;
    access_log off;
    add_header Cache-Control "public, max-age=31536000, immutable";
}

location / {
    proxy_pass http://127.0.0.1:8000;
    include proxy_params;
}
```

## Use cases

The project can serve as:

- An online resource for students and teachers
- A data source for mobile apps and other services via the REST API
- A foundation for an extensible electronic dictionary that can import existing datasets

## Licensing

The source code is distributed under the terms of the MIT License. Dictionary data and other textual content are provided under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. This allows reuse in search engines, academic research and training language models.

