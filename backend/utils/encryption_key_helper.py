def is_valid_key(key: str) -> bool:
    # Fernet keys are 44‑char base64 strings (32‑byte raw key).
    return isinstance(key, str) and len(key) == 44
