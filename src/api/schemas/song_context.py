from marshmallow import Schema, fields

class SongContextSchema(Schema):
    Id = fields.Int()
    Name = fields.Str()
    Year = fields.Int()
    Artist = fields.Str()
    Shortname = fields.Str()
    Bpm = fields.Int()
    Duration = fields.Int()
    Genre = fields.Str()
    SpotifyId = fields.Str()
    Album = fields.Str()