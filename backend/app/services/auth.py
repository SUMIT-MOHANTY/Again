import hashlib, hmac, base64, time
from ..config import settings

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

def verify_password(pw: str, hashed: str) -> bool:
    return hash_password(pw) == hashed

def create_jwt(data: dict, ttl: int = 3600) -> str:
    header = base64.urlsafe_b64encode(b'{"alg":"HS256","typ":"JWT"}').rstrip(b'=')
    payload = data.copy()
    payload.update({"exp": int(time.time()) + ttl})
    payload_bytes = str(payload).encode()
    payload_enc = base64.urlsafe_b64encode(payload_bytes).rstrip(b'=')
    signature = hmac.new(settings.JWT_SECRET.encode(), header + b'.' + payload_enc, hashlib.sha256).digest()
    sig_enc = base64.urlsafe_b64encode(signature).rstrip(b'=')
    return b'.'.join([header, payload_enc, sig_enc]).decode()

def verify_jwt(token: str) -> dict | None:
    try:
        header_b, payload_b, sig_b = token.split('.')
        expected_sig = hmac.new(settings.JWT_SECRET.encode(), f"{header_b}.{payload_b}".encode(), hashlib.sha256).digest()
        if not hmac.compare_digest(base64.urlsafe_b64encode(expected_sig).rstrip(b'='), sig_b.encode()):
            return None
        payload_json = base64.urlsafe_b64decode(payload_b + '==')
        payload = eval(payload_json.decode())  # safe for mock, replace with json.loads in prod
        if payload.get('exp', 0) < int(time.time()):
            return None
        return payload
    except Exception:
        return None
