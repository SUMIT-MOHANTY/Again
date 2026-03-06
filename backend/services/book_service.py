from ..models.book import Book
from ..cache.redis_client import redis_get, redis_set
from ..cache.cache_keys import cache_key_book
from ..utils.performance_logger import log_execution
@log_execution('book_service.get_book')
def get_book(book_id: int):
    key = cache_key_book(book_id)
    cached = redis_get(key)
    if cached:
        return cached  # raw bytes; downstream serialization will handle
    book = Book.query.get(book_id)
    if book:
        redis_set(key, str(book.id), ttl=600)
    return book
