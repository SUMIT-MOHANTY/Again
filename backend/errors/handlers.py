from flask import jsonify
from .exceptions import APIException

def register_error_handlers(app):
    @app.errorhandler(APIException)
    def handle_api_exception(error):
        response = {
            "status": "error",
            "message": error.message,
            "details": error.details
        }
        return jsonify(response), error.status_code

    @app.errorhandler(400)
    def handle_bad_request(error):
        return jsonify({"status": "error", "message": "Bad request", "details": {}}), 400

    @app.errorhandler(401)
    def handle_unauthorized(error):
        return jsonify({"status": "error", "message": "Unauthorized", "details": {}}), 401

    @app.errorhandler(403)
    def handle_forbidden(error):
        return jsonify({"status": "error", "message": "Forbidden", "details": {}}), 403

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({"status": "error", "message": "Not found", "details": {}}), 404

    @app.errorhandler(409)
    def handle_conflict(error):
        return jsonify({"status": "error", "message": "Conflict", "details": {}}), 409

    @app.errorhandler(500)
    def handle_internal_error(error):
        return jsonify({"status": "error", "message": "Internal server error", "details": {}}), 500
