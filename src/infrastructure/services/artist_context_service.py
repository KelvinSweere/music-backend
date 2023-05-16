from src.infrastructure.models.artist_context import ArtistContext
from src.infrastructure.databases import sqlalchemy_db as db

class ArtistContextService:

		def create_artist(self, data):
			artist_context = ArtistContext(**data)

			db.session.add(artist_context)
			db.session.commit()
			return artist_context

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