from marshmallow import Schema, fields

class UserCreateRequestSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class UserUpdateRequestSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class UserPatchRequestSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()

class UserResponseSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    created_at = fields.Str()
