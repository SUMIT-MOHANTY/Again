import redis, os
from ..config import Config
_redis = None
def get_redis():
    global _redis
    if _redis is None:
        _redis = redis.from_url(Config.REDIS_URL, decode_responses=True)
    return _redis
