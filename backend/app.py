from . import create_app
from .config import Config

if __name__ == '__main__':
    app = create_app()
    # Run with self‑signed TLS certificates
    app.run(host='0.0.0.0', port=5000, ssl_context=(Config.CERT_PATH, Config.KEY_PATH))
