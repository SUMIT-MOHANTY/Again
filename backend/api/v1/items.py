from flask import jsonify
from . import api_v1
from ...schemas.item import ItemListResponseSchema

@api_v1.route('/items', methods=['GET'])
def list_items():
    # Placeholder empty list response
    response = {"items": [], "page": 1, "total": 0}
    return jsonify(ItemListResponseSchema().dump(response)), 200
