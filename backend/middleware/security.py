def apply_security_headers(app):
    @app.after_request
    def add_hsts(response):
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    try:
        from flask_talisman import Talisman
        Talisman(app, force_https=False)
    except Exception:
        pass
