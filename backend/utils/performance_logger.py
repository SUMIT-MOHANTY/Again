from time import perf_counter
def log_execution(endpoint_name: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = perf_counter()
            result = func(*args, **kwargs)
            elapsed = (perf_counter() - start) * 1000
            print(f"[PERF] {endpoint_name} took {elapsed:.2f}ms")
            return result
        return wrapper
    return decorator
