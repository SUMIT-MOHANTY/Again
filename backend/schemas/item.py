from marshmallow import Schema, fields

class ItemListResponseSchema(Schema):
    items = fields.List(fields.Dict())
    page = fields.Int()
    total = fields.Int()
