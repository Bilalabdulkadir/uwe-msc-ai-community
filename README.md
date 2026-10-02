# UWE MSc AI Community Platform

A full-stack community platform for MSc Artificial Intelligence students, researchers, alumni, and industry professionals at UWE Bristol.

The platform is designed to support collaboration, research sharing, mentorship, project development, and lifelong academic engagement within the UWE AI community. It combines a FastAPI backend, PostgreSQL data model, Next.js frontend, and Docker-based local development environment to provide a scalable MVP foundation for future AI-powered features.

Built with FastAPI, PostgreSQL, Next.js, and Docker, the project provides a strong base for future capabilities such as semantic search, recommendations, intelligent community assistance, and richer AI-driven engagement workflows.

## Current status

The project is currently in a scaffolded MVP phase with the following in place:

- PostgreSQL schema and seed data
- FastAPI backend scaffold with SQLAlchemy async support
- Pydantic v2 data validation
- JWT-ready authentication helpers
- Next.js App Router frontend scaffold
- Docker Compose local development setup
- Alembic migration starter
- PostgreSQL reference documentation for materialized views and temp tables

## Tech stack

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
- Responsive UI structure
- API-ready frontend layer

### Infrastructure
- Docker Compose
- PostgreSQL container
- Environment configuration via .env.example

## Repository structure

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
├── LICENSE
└── .github/
```

## Documentation

- docs/SETUP.md — local development and setup instructions
- docs/postgres-materialized-views-quick-ref.md — quick-reference guide for CTEs, temp tables, and materialized views
- docs/postgres-temp-tables-materialized-views.md — deeper PostgreSQL reference covering security-restricted operations and migration trade-offs
- schema/schema.sql — PostgreSQL database schema
- schema/seed.sql — demo seed data

## Core domain areas

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

This gives the project a solid foundation for a future AI-enhanced community experience while keeping the MVP logically structured and extensible.

## Local development

1. Clone the repository:

```bash
git clone https://github.com/Bilalabdulkadir/uwe-msc-ai-community.git
cd uwe-msc-ai-community
```

2. Copy the environment file:

```bash
cp .env.example .env
```

3. Build and start the stack:

```bash
docker compose up --build
```

4. Access the application:

- Frontend: http://localhost:3000/
- Backend: http://localhost:8000/
- API docs: http://localhost:8000/docs

## Database setup

The schema is designed for PostgreSQL 18 compatibility and is intended to remain compatible with a future pgEdge/PostgreSQL environment.

To initialise the database manually:

```bash
docker compose exec db psql -U uwe -d uwe_community -f /docker-entrypoint-initdb.d/schema.sql
```

For a fresh local environment, you can also use the schema file in the repository with your preferred PostgreSQL client.

## API overview

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

## Frontend pages

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

These pages are intentionally structured as a starting point and can be expanded with real data fetching and richer UI components.

## Security notes

- credentials are stored as hashed values
- JWT secrets and sensitive environment variables are kept in .env and not committed to source control
- no production credentials are included in the repository

## PR-ready changelog template

```markdown
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
- Added PostgreSQL reference material for temp tables and materialized views

### Future work

- Full CRUD validation
- Authentication and RBAC
- Frontend data integration
- Search and filtering
- Advanced dashboards
- AI-assisted community features
- Cloud deployment
```

## Suggested repository description

> AI-powered community platform for UWE MSc Artificial Intelligence students featuring discussions, projects, events, resources, mentorship, publications, and future semantic-search capabilities.

## Roadmap

### Next milestones
1. complete CRUD validation and service consistency across all models
2. add stronger role-based access and authentication flows (JWT)
3. add real frontend data fetching and forms
4. add Alembic migration execution for production-ready database management
5. add richer dashboards and search/filtering
6. add AI features such as semantic search and community assistant
7. deploy to cloud hosting and database infrastructure

## Notes

This repository is intentionally structured to support a scalable MVP and future AI-enabled platform features without prematurely hard-coding RAG or vector-search logic.

---

Project developed for the UWE MSc AI Community Platform initiative.
