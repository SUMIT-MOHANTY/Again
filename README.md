# Feature‑Flag Service (Backend Prototype)

## Current Implementation
The service stores flags in an in‑memory dictionary defined in `backend/config.py`.
At startup the environment variable `FEATURE_FLAGS` can contain a JSON string that
pre‑populates this dictionary; otherwise it defaults to an empty dict.
All flag operations (`list`, `get`, `set`) are performed against this dict via the
`FlagService` class. The FastAPI app exposes two endpoints:
- `GET /api/v1/flags` - returns all flags.
- `POST /api/v1/flags/{name}` - creates or updates a flag.

## Future Migration
To replace the in‑memory store with Redis or a relational database:
1. Implement a `FlagRepository` interface with methods `list`, `get`, `set`.
2. Provide concrete classes, e.g. `RedisFlagRepository` (using `redis-py`) or
   `SQLFlagRepository` (using SQLAlchemy).
3. Update `backend/api/dependencies.py` to return an instance of the chosen
   repository instead of the raw dict.
4. Adjust `FlagService` to accept a repository rather than a dict, delegating all
   persistence operations to it. The FastAPI routers remain unchanged because
   they depend only on the service layer.
