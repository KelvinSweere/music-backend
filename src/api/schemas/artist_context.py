from marshmallow import Schema, fields

class ArtistContextSchema(Schema):
    Id = fields.Int()
    Name = fields.Str()
