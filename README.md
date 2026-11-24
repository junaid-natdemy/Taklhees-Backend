# Taklhees-Backend

Centralized Django 5.1+ REST API backend for **Takhlees Business**, serving corporate document clearing, typing, government PRO services in the UAE and Takhlees Career Academy in India.

## Tech Stack
- **Runtime**: Python 3.12+ (Python 3.13)
- **Framework**: Django 5.1+ & Django REST Framework (DRF)
- **Database**: PostgreSQL with `psycopg` (v3)
- **Authentication**: Django Auth + SimpleJWT (Bearer tokens)
- **Documentation**: drf-spectacular (OpenAPI 3.0 & Swagger UI)
- **Middleware**: django-cors-headers, django-environ, django-filter

## 13 Modular Applications
- `accounts`: User roles, permissions & authentication
- `pages`: Static & legal page CMS
- `services`: UAE typing, document clearing & PRO services CMS
- `branches`: UAE branch network locator CMS
- `courses`: India career academy course catalog
- `teachers`: Faculty profiles & assigned course links
- `admissions`: Online enrollment & student admissions
- `enquiries`: General & service lead pipeline
- `testimonials`: Client & student reviews
- `gallery`: Photos & event media albums
- `blog`: Industry insights & visa guides
- `careers`: Job openings & applicant CV tracking
- `integrations`: CRM / HRMS webhook dispatch & synchronization

## Getting Started
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/development.txt
python manage.py migrate
python manage.py runserver
```

## Audit & Changelog
Full engineering audit trail documented in [CHANGELOG.md](./CHANGELOG.md).
