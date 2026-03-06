# Feature Flags

## Current implementation

- Flags are stored in the in‑memory dictionary `FEATURE_FLAGS`.
- At startup `load_feature_flags()` parses the JSON string from the environment variable `FEATURE_FLAGS_JSON` and populates the store with `FeatureFlag` dataclass instances.
- Admin API (`/api/flags`) allows reading all flags and toggling a single flag.  Admin access is mocked via the `X-Admin` request header.

## Migration plan

1. **Introduce Redis** - Create a Redis client (e.g. `redis.Redis.from_url(os.getenv('REDIS_URL'))`).
2. **Replace store functions** - `load_feature_flags` will fetch a hash from Redis, and CRUD operations in the API will `hset`/`hget` the flag data.
3. **Persist across restarts** - Flags will survive process restarts as they are kept in Redis.
4. **Optional DB fallback** - Implement a SQLAlchemy model `FeatureFlagModel` with columns `name`, `enabled`, `description` for environments without Redis.
5. **Update type hints** - Adjust return types to `Mapping[str, FeatureFlag]` and add proper Pydantic schemas for the API payloads.

The existing tests continue to pass with the in‑memory store, ensuring a smooth transition when the persistent layer is added.
