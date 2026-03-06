from flask import jsonify

def health():
    return jsonify(status='ok'), 200

def get_items():
    # Placeholder implementation - returns static list
    return jsonify(items=[]), 200
