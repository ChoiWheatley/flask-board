from marshmallow import Schema, fields


class PostSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
