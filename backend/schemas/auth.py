from marshmallow import Schema, fields

class LoginRequestSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class AuthResponseSchema(Schema):
    access_token = fields.Str()
    token_type = fields.Str()
