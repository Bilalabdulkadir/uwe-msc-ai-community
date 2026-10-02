# Project setup & run instructions

This repository now contains a scaffold for the UWE MSc AI Community Platform.

Quick start (development, from repository root):

1. Copy example environment variables
   cp .env.example .env

2. Start services with Docker Compose
   docker compose up --build

3. Initialize the database schema and seed data (once the DB is ready):
   # run these after db service is accepting connections
   docker compose exec -T backend bash -lc "psql $DATABASE_URL -f /workdir/schema/schema.sql"
   # or run via psql from your host

Backend API:
- http://localhost:8000/
- Health: http://localhost:8000/health
- Users: http://localhost:8000/api/users

Frontend:
- http://localhost:3000/

Development notes
- Backend uses FastAPI + SQLAlchemy (async) + asyncpg
- Use Alembic for migrations (see backend/README or Alembic docs)

