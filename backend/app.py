from flask import Flask, request, redirect, jsonify
from .middleware.security import apply_security_headers

def create_app():
    app = Flask(__name__)
    apply_security_headers(app)

    @app.before_request
    def enforce_https():
        if request.is_secure or request.headers.get('X-Forwarded-Proto', '').lower() == 'https':
            return
        url = request.url.replace('http://', 'https://')
        return redirect(url, code=301)

    @app.route('/health')
    def health():
        return jsonify({"status":"success","data":{"alive":True},"error":None})

    return app

app = create_app()
