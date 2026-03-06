import json
from flask import Response
from ..config import DEFAULT_API_VERSION, SUPPORTED_VERSIONS

def versioning_middleware(app):
    def middleware(environ, start_response):
        path = environ.get('PATH_INFO', '')
        if path.startswith('/api/'):
            # Strip '/api/' and split the remainder
            remainder = path[5:]
            parts = remainder.split('/', 1)
            version = parts[0] if parts[0] else ''
            # No version supplied -> prepend default
            if not version:
                new_path = f"/api/{DEFAULT_API_VERSION}/" + (parts[1] if len(parts) > 1 else '')
                environ['PATH_INFO'] = new_path.rstrip('/')
                return app(environ, start_response)
            # Unsupported version
            if version not in SUPPORTED_VERSIONS:
                body = json.dumps({"error": "API version not supported", "supported_versions": SUPPORTED_VERSIONS})
                resp = Response(body, status=404, mimetype='application/json')
                return resp(environ, start_response)
        return app(environ, start_response)
    return middleware
