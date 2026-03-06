from flask import request, jsonify, current_app
from ..utils.redis_client import get_redis
class RateLimiter:
    def __init__(self, app=None):
        if app:
            self.init_app(app)
    def init_app(self, app):
        app.before_request(self.check_limit)
    def _key(self):
        # Use authenticated user id if present, else IP address
        user = getattr(request, 'user', None)
        if user and getattr(user, 'id', None):
            return f"rl:user:{user.id}"
        return f"rl:ip:{request.remote_addr}"
    def check_limit(self):
        cfg = current_app.config
        limit = cfg.get('RATE_LIMIT', 5)
        window = cfg.get('RATE_WINDOW', 60)
        key = self._key()
        r = get_redis()
        # Increment counter atomically
        count = r.incr(key)
        if count == 1:
            r.expire(key, window)
        if count > limit:
            retry = r.ttl(key)
            return (jsonify({
                'error':'rate limit exceeded',
                'retry_after_seconds':retry
            }), 429)
        # Add rate-limit headers for client visibility
        remaining = max(limit - count, 0)
        request.headers.environ['HTTP_X_RATE_LIMIT_LIMIT'] = str(limit)
        request.headers.environ['HTTP_X_RATE_LIMIT_REMAINING'] = str(remaining)
        request.headers.environ['HTTP_X_RATE_LIMIT_RESET'] = str(r.ttl(key))
