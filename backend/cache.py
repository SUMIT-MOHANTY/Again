import os
import json
from redis.asyncio import Redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis = Redis.from_url(REDIS_URL, decode_responses=True)

async def get(key: str):
    data = await redis.get(key)
    return json.loads(data) if data else None

async def set(key: str, value, ttl: int = 300):
    await redis.set(key, json.dumps(value), ex=ttl)

async def invalidate(key: str):
    await redis.delete(key)
