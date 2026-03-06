from .app import create_app
from .config import CERT_PATH, KEY_PATH

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443, ssl_context=(CERT_PATH, KEY_PATH))
