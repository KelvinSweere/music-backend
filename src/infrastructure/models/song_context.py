from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.model_extension import ModelExtension


class SongContext(db.Model, ModelExtension):
    __tablename__ = 'song_context'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, default=False)
    Year = db.Column(db.Integer, default=False)
    Artist = db.Column(db.String, default=False)
    Shortname = db.Column(db.String, default=False)
    Bpm = db.Column(db.Integer, default=0)
    Duration = db.Column(db.Integer, default=False)
    Genre = db.Column(db.String, default=False)
    SpotifyId = db.Column(db.String, default=False)
    Album = db.Column(db.String, default=False)