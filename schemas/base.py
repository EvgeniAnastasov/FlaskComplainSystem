from marshmallow import Schema, fields


class UserRequestBase(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
