# UWE MSc AI Community Platform

A full-stack community platform for MSc Artificial Intelligence students, researchers, alumni and industry professionals at UWE Bristol.

The platform supports collaboration, research sharing, mentorship and project development within the UWE AI community. It combines a FastAPI backend, a PostgreSQL data model, a Next.js frontend and a Docker-based development environment, giving a scalable MVP foundation for future AI-powered features such as semantic search, recommendations and an intelligent community assistant.

**Status:** scaffolded MVP. The core structure is in place and features are still being built out (see the [Roadmap](#roadmap)).

## Table of contents

- [Features](#features)
- [Tech stack](#tech-stack)
- [Quick start](#quick-start)
- [Database setup](#database-setup)
- [Repository structure](#repository-structure)
- [API overview](#api-overview)
- [Frontend pages](#frontend-pages)
- [Documentation](#documentation)
- [Security notes](#security-notes)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Author and licence](#author-and-licence)

## Features

Implemented in the current scaffold:

- PostgreSQL schema and seed data
- FastAPI backend with async SQLAlchemy and a service-layer structure
- Pydantic v2 data validation
- JWT-ready authentication helpers
- Next.js App Router frontend scaffold (TypeScript)
- Docker Compose local development setup
- Alembic migration starter
- PostgreSQL reference documentation for materialized views and temp tables

Core domain models: users, profiles, discussions, discussion comments, events, projects, resources, publications, mentorships and notifications.

## Tech stack

| Layer | Technologies |
| --- | --- |
| Backend | Python 3.11, FastAPI, SQLAlchemy 2.x (async), asyncpg, Pydantic v2, Alembic, JWT-ready auth helpers |
| Database | PostgreSQL (schema designed for PostgreSQL 18 compatibility) |
| Frontend | Next.js App Router, TypeScript, responsive UI structure, API-ready frontend layer |
| Infrastructure | Docker Compose, PostgreSQL container, `.env`-based configuration |

## Quick start

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

4. Open the application:

   | Service | URL |
   | --- | --- |
   | Frontend | http://localhost:3000/ |
   | Backend | http://localhost:8000/ |
   | API docs | http://localhost:8000/docs |

See [`docs/SETUP.md`](docs/SETUP.md) for detailed setup instructions.

## Database setup

The schema targets PostgreSQL 18 and is intended to stay compatible with a future pgEdge/PostgreSQL environment.

To initialise the database manually:

```bash
docker compose exec db psql -U uwe -d uwe_community -f /docker-entrypoint-initdb.d/schema.sql
```

You can also apply `schema/schema.sql` with any PostgreSQL client. `schema/seed.sql` contains demo data for local development.

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

## API overview

The backend exposes endpoints for health checks, users, profiles, discussions, comments, events, projects, resources, publications, mentorships and notifications. Interactive documentation is available at `/docs` when the backend is running.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/health` | Health check |
| GET | `/api/users/` | List users |
| GET | `/api/events/` | List events |
| GET | `/api/projects/` | List projects |
| GET | `/api/resources/` | List resources |
| GET | `/api/discussions/` | List discussions |

## Frontend pages

The scaffold includes initial pages for `/`, `/dashboard`, `/community`, `/discussions`, `/events`, `/projects`, `/resources`, `/mentorship` and `/publications`. They are a starting point, ready to be expanded with real data fetching and richer UI components.

## Documentation

| File | Purpose |
| --- | --- |
| [`docs/SETUP.md`](docs/SETUP.md) | Local development and setup instructions |
| [`docs/postgres-materialized-views-quick-ref.md`](docs/postgres-materialized-views-quick-ref.md) | Quick reference for CTEs, temp tables and materialized views |
| [`docs/postgres-temp-tables-materialized-views.md`](docs/postgres-temp-tables-materialized-views.md) | Deeper reference on security-restricted operations and migration trade-offs |
| [`schema/schema.sql`](schema/schema.sql) | PostgreSQL database schema |
| [`schema/seed.sql`](schema/seed.sql) | Demo seed data |

## Security notes

- Credentials are stored as hashed values.
- JWT secrets and other sensitive settings live in `.env` and are not committed to source control.
- No production credentials are included in the repository.

## Roadmap

- [ ] Complete CRUD validation and service consistency across all models
- [ ] Stronger authentication and role-based access control (JWT)
- [ ] Real frontend data fetching and forms
- [ ] Alembic migration execution for production-ready database management
- [ ] Richer dashboards, search and filtering
- [ ] AI features such as semantic search and a community assistant
- [ ] Cloud deployment (hosting and database infrastructure)

The project is deliberately structured to support a scalable MVP and future AI features without prematurely hard-coding RAG or vector-search logic.

## Contributing

Contributions and ideas are welcome. Please open an issue to discuss a change, then submit a pull request that follows the pull request template in `.github/`.

## Author and licence

Created by [Bilal Abdulkadir Muhammed](https://github.com/Bilalabdulkadir) as part of the UWE MSc AI Community Platform initiative.

Released under the licence in [`LICENSE`](LICENSE).
