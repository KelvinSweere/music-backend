from src.infrastructure.models.artist_context import ArtistContext
from src.infrastructure.databases import sqlalchemy_db as db
from flask import abort

class ArtistContextService:

		def create_artist(self, data):
			if self.get_artist_by_id(data['Id']) is not None:
					return abort(409, 'A artist with the provided ID already exists.')
			try:
				artist_context = ArtistContext(**data)
				db.session.add(artist_context)
				db.session.commit()
				return artist_context
			except Exception as e:
				return abort(400, e)
		
		def get_all_artists(self):
			artist_context = ArtistContext.query.all()
			return artist_context

		def get_artist_by_id(self, id: int):
			artist_context = ArtistContext.query.get(id)
			return artist_context
		
		def update_artist(self, id: int, data):
			artist_context = ArtistContext.query.get(id)
			artist_context.update(db, data)
			return artist_context

		def delete_artist(self, id: int):
			artist_context = ArtistContext.query.get(id)
			if(artist_context is not None):
				artist_context.delete(db)
			return artist_context