from marshmallow import Schema, fields


class ArtistContextSchema(Schema):
    id = fields.Int()
    name = fields.Str()
