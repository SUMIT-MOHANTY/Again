from ..models.transaction import Transaction
from ..cache.redis_client import redis_get, redis_set
from ..cache.cache_keys import cache_key_transaction
from ..utils.performance_logger import log_execution
@log_execution('transaction_service.get_transaction')
def get_transaction(tx_id: int):
    key = cache_key_transaction(tx_id)
    cached = redis_get(key)
    if cached:
        return cached
    tx = Transaction.query.get(tx_id)
    if tx:
        redis_set(key, str(tx.id), ttl=600)
    return tx
