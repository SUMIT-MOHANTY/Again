import time, requests
BASE_URL = 'http://localhost:5000/api'
THRESHOLD_MS = 250
def _measure(endpoint):
    start = time.perf_counter()
    r = requests.get(f"{BASE_URL}{endpoint}")
    elapsed = (time.perf_counter() - start) * 1000
    assert r.status_code == 200
    assert elapsed <= THRESHOLD_MS, f"{endpoint} took {elapsed:.2f}ms"
def test_book():
    _measure('/books/1')
def test_member():
    _measure('/members/1')
def test_transaction():
    _measure('/transactions/1')
