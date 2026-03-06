import redis
from ..config import Config
redis_client = redis.Redis.from_url(Config.REDIS_URL)
def redis_get(key):
    return redis_client.get(key)
def redis_set(key, value, ttl=300):
    redis_client.setex(key, ttl, value)
