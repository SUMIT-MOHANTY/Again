from flask import Flask, jsonify
from .config import config
from .api.prompt import bp as prompt_bp

app = Flask(__name__)
app.register_blueprint(prompt_bp, url_prefix='/api')

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'postgres_uri': config.POSTGRES_URI})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
