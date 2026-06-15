# TaskFlow API

![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi)
![Architecture](https://img.shields.io/badge/architecture-Clean%20Architecture-success)

A modular, architected backend for **TaskFlow**. A collaborative task management platform (think a lightweight Jira/Trello), built with FastAPI.

## Overview

This is a backend service for a full-stack collaborative task management system.

The long-term scope includes user authentication and roles, projects with boards and columns, tasks, comments, real-time notifications via WebSockets and a React + TypeScript frontend.

## Current Status

In development.

The core application architecture is complete: modular project structure, dependency injection, repository pattern, environment-based configuration, centralized error handling and structured logging. 
Storage currently uses an in-memory implementation as a placeholder; PostgreSQL integration is the next step.

## Tech Stack

**Implemented**
- FastAPI
- Pydantic / pydantic-settings
- Uvicorn

**Planned**
- PostgreSQL + SQLAlchemy + Alembic
- JWT authentication and role-based access control
- WebSockets for real-time notifications
- Pytest test suite
- Docker and Docker Compose
- React + TypeScript frontend

## Architecture

The application follows a layered architecture with dependency inversion:

```
Router (HTTP)  ->  Service (business logic)  ->  Repository (data access)
```

- **Routers** (`api/v1/endpoints/`) handle HTTP concerns only — request/response
  shapes, status codes.
- **Services** (`services/`) contain business rules and orchestration. They
  depend on repository *interfaces* (`typing.Protocol`), not concrete
  implementations.
- **Repositories** (`repositories/`) abstract data access. The current
  implementation is in-memory; a SQLAlchemy-based implementation will be added
  later without changing services or routers.
- **Configuration** (`core/config.py`) is environment-based via
  `pydantic-settings`, with validated, typed settings loaded from `.env`.
- **Error handling** (`core/exceptions.py`, `core/exception_handlers.py`) uses
  a custom exception hierarchy mapped to HTTP responses through a single
  global handler.
- **Logging** (`core/logging.py`, `core/middleware.py`) provides structured,
  per-module logging plus request-level logging middleware.

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone https://github.com/hiri-code/taskflow-api.git
cd taskflow-api

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
```

Adjust the values in `.env` as needed.

### Run the development server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`, with interactive
documentation at `http://localhost:8000/docs`.

## Roadmap

- [x] Modular project structure
- [x] Routers → Services → Repositories (Clean Architecture)
- [x] Dependency injection
- [x] Environment-based configuration
- [x] Centralized exception handling
- [x] Structured logging
- [ ] PostgreSQL + SQLAlchemy 2.0
- [ ] Database migrations with Alembic
- [ ] JWT authentication & roles
- [ ] WebSockets for real-time notifications
- [ ] Automated test suite (pytest)
- [ ] Docker & deployment
- [ ] React + TypeScript frontend