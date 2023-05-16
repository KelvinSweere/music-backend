from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.model_extension import ModelExtension


class ArtistContext(db.Model, ModelExtension):
    __tablename__ = 'artist_context'
    ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String, default=False)
