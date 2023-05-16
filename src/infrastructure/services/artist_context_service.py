from src.infrastructure.models.artist_context import ArtistContext
from src.infrastructure.databases import sqlalchemy_db as db

class ArtistContextService:

		def create_artist(self, data):
			artist_context = ArtistContext()
			artist_context.ID = data['Id']
			artist_context.NAME = data['Name']

			db.session.add(artist_context)
			db.session.commit()
			return artist_context

		def get_all_artists(self):
			artist_context = ArtistContext.query.first()
			return artist_context

		def get_artist_by_id(self, id: int):
			status = ArtistContext.query.first()

			if status is None:
				status = ArtistContext()
				status.save(db)

			return status
		
		def update_artist(self, id: int, data):
			artist_context = ArtistContext.query.first()
			return artist_context

		def delete_artist(self, id: int):
			artist_context = ArtistContext.query.first()
			return artist_context