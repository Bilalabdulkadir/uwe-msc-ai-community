# UWE MSc AI Community Platform

A full-stack AI-powered community platform for MSc Artificial Intelligence students, researchers, alumni, and industry professionals.

## Current status

- PostgreSQL schema and seed data are in place
- FastAPI backend scaffolded with SQLAlchemy async and Pydantic v2
- Next.js frontend scaffolded with App Router
- Docker Compose setup provided for local development

## Architecture

### Frontend
- Next.js App Router
- TypeScript
- Responsive UI structure

### Backend
- FastAPI
- SQLAlchemy 2.x async
- Pydantic v2
- PostgreSQL 18-compatible schema
- JWT-ready auth helpers

### Database
- PostgreSQL 18-compatible
- Schema is designed for future pgEdge / pgvector integration

## Run locally

1. Copy environment file:
   cp .env.example .env

2. Build and run the stack:
   docker compose up --build

3. Database initialization:
   docker compose exec db psql -U uwe -d uwe_community -f /docker-entrypoint-initdb.d/schema.sql

4. Access services:
   - Frontend: http://localhost:3000/
   - Backend: http://localhost:8000/
   - API docs: http://localhost:8000/docs

## Core API routes

- GET /health
- GET /api/users/
- GET /api/profiles/
- GET /api/discussions/
- GET /api/events/
- GET /api/projects/
- GET /api/resources/
- GET /api/publications/
- GET /api/mentorships/
- GET /api/notifications/

## Notes

- The project intentionally keeps the data model extensible for future AI/RAG features.
- Secrets should be managed with environment variables rather than committed to source control.
