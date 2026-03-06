from ..models.member import Member
from ..cache.redis_client import redis_get, redis_set
from ..cache.cache_keys import cache_key_member
from ..utils.performance_logger import log_execution
@log_execution('member_service.get_member')
def get_member(member_id: int):
    key = cache_key_member(member_id)
    cached = redis_get(key)
    if cached:
        return cached
    member = Member.query.get(member_id)
    if member:
        redis_set(key, str(member.id), ttl=600)
    return member
