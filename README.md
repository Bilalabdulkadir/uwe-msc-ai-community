# UWE MSc AI Community Platform

A full-stack community platform for MSc Artificial Intelligence students, researchers, alumni, and industry professionals at UWE Bristol.

A modern community platform for MSc Artificial Intelligence students at UWE Bristol, designed to support collaboration, research sharing, networking, mentorship, project development, and lifelong academic engagement.

Built with FastAPI, PostgreSQL, Next.js, and Docker, the platform provides a scalable foundation for future AI-powered features such as semantic search, recommendations, and intelligent community assistance.

## Project Status

Current status of the scaffolded milestone:
- PostgreSQL 18-compatible schema created
- SQLAlchemy async models and Pydantic schemas added
- FastAPI backend routes for core domain entities implemented
- JWT-ready auth helpers and password hashing included
- Next.js App Router frontend scaffold added
- Docker Compose development environment added
- Alembic migration starter included
- PostgreSQL reference documentation for materialized views and temp tables added

## Tech Stack

### Backend
- Python 3.11
- FastAPI
- SQLAlchemy 2.x (async)
- Pydantic v2
- PostgreSQL 18-compatible schema
- Alembic
- asyncpg
- JWT-ready auth helpers

### Frontend
- Next.js App Router
- TypeScript
- Responsive page structure
- API-ready frontend layer

### Infrastructure
- Docker Compose
- PostgreSQL container
- Development environment configuration via .env.example

## Repository Structure

```text
uwe-msc-ai-community/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── db.py
│   │   └── main.py
│   ├── tests/
│   ├── alembic/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── alembic.ini
├── web/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── Dockerfile
│   ├── package.json
│   └── README.md
├── schema/
│   ├── schema.sql
│   └── seed.sql
├── docs/
│   ├── SETUP.md
│   ├── postgres-materialized-views-quick-ref.md
│   └── postgres-temp-tables-materialized-views.md
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

## Documentation

- docs/SETUP.md — development and run instructions
- docs/postgres-materialized-views-quick-ref.md — quick-reference guide for CTEs, temp tables, and materialized views
- docs/postgres-temp-tables-materialized-views.md — deeper PostgreSQL reference covering security-restricted operations and migration trade-offs
- schema/schema.sql — PostgreSQL 18-compatible schema
- schema/seed.sql — sensible demo seed data

## Core Domain Areas

The platform currently includes these core model groups:
- users
- profiles
- discussions
- discussion comments
- events
- projects
- resources
- publications
- mentorships
- notifications

This gives the platform a solid foundation for a future AI-enhanced community experience while keeping the MVP logically organised.

## Local Development Setup

1. Clone the repository

```bash
git clone https://github.com/Bilalabdulkadir/uwe-msc-ai-community.git
cd uwe-msc-ai-community
```

2. Copy environment variables

```bash
cp .env.example .env
```

3. Build and start the stack

```bash
docker compose up --build
```

4. Access the services

- Frontend: http://localhost:3000/
- Backend: http://localhost:8000/
- API docs: http://localhost:8000/docs

## Database Setup

The schema is designed for PostgreSQL 18 compatibility and is intended to be compatible with a future pgEdge PostgreSQL 18 environment.

To initialise the database manually:

```bash
docker compose exec db psql -U uwe -d uwe_community -f /docker-entrypoint-initdb.d/schema.sql
```

Or for a fresh local environment, use the schema file in the repo and run it with your preferred Postgres client.

## API Overview

The backend exposes core endpoints for:
- health checks
- users
- profiles
- discussions
- comments
- events
- projects
- resources
- publications
- mentorships
- notifications

Examples:

```text
GET /health
GET /api/users/
GET /api/events/
GET /api/projects/
GET /api/resources/
GET /api/discussions/
```

## Frontend Pages

The scaffold includes initial pages for:
- /
- /dashboard
- /community
- /discussions
- /events
- /projects
- /resources
- /mentorship
- /publications

These pages are intentionally structured as a starting point and can be expanded with real data fetching and UI components.

## Security Notes

- credentials are stored as hashed values
- JWT secret and other env values are kept in .env and not committed to source control
- no production credentials are included in the repository

## PR-ready Changelog Template (use in PR descriptions)

```
## Summary

This PR introduces the initial project scaffold for the UWE MSc AI Community Platform.

### Added

- FastAPI backend structure
- Async SQLAlchemy setup
- PostgreSQL schema and seed data
- Core domain models:
  - Users
  - Profiles
  - Discussions
  - Comments
  - Events
  - Projects
  - Resources
  - Publications
  - Mentorships
  - Notifications
- Pydantic schemas
- Service-layer architecture
- API routing structure
- JWT-ready authentication helpers
- Next.js App Router frontend scaffold
- Docker Compose local development environment
- Alembic migration starter
- Environment configuration templates
- Setup documentation
- PostgreSQL materialized-view quick-reference documentation

### Documentation

- Added repository setup instructions
- Added architecture overview
- Added development workflow guidance
- Documented roadmap and future milestones
- Added PostgreSQL quick-reference material for temp tables and materialized views

### Future Work

- Full CRUD validation
- Authentication and RBAC
- Frontend data integration
- Search and filtering
- Advanced dashboards
- AI-assisted community features
- Cloud deployment
```

## Suggested GitHub repository description

> AI-powered community platform for UWE MSc Artificial Intelligence students featuring discussions, projects, events, resources, mentorship, publications, and future semantic-search capabilities.

## Roadmap

### Next Milestones
1. complete CRUD validation and service consistency across all models
2. add stronger role-based access and authentication flows (JWT)
3. add real frontend data fetching and forms
4. add Alembic migration execution for production-ready database management
5. add richer dashboards and search/filtering
6. add AI features such as semantic search and community assistant
7. deploy to cloud hosting and database infrastructure

## Notes

This repository is intentionally structured to support a scalable MVP and future AI-enabled platform features without prematurely hard-coding RAG or vector search logic.

---

Project developed for the UWE MSc AI Community Platform initiative.
