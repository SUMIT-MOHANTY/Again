def cache_key_book(book_id: int) -> str:
    return f"book:{book_id}"
def cache_key_member(member_id: int) -> str:
    return f"member:{member_id}"
def cache_key_transaction(tx_id: int) -> str:
    return f"transaction:{tx_id}"
