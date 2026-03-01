from flask import Flask, jsonify
from errors.handlers import register_error_handlers
from errors.exceptions import NotFoundError

def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.update(config)

    register_error_handlers(app)

    @app.route("/api/v1/health")
    def health():
        from datetime import datetime
        return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

    @app.route("/api/v1/users", methods=["POST"])
    def create_user():
        from schemas.user import UserCreateSchema
        from flask import request
        data = request.get_json()
        try:
            validated = UserCreateSchema(**data)
            return jsonify({"status": "success", "data": validated.model_dump()}), 201
        except Exception as e:
            raise NotFoundError(str(e), {"code": "VALIDATION_ERROR"})

    @app.route("/api/v1/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        if user_id <= 0:
            raise NotFoundError("Invalid user ID", {"field": "user_id"})
        return jsonify({"status": "success", "data": {"id": user_id, "email": "test@example.com", "name": "Test", "created_at": "2024-01-01T00:00:00"}}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
