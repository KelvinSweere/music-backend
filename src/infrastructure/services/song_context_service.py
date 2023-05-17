from src.infrastructure.models.song_context import SongContext
from src.infrastructure.databases import sqlalchemy_db as db
from flask import abort

class SongContextService:

		def create_song(self, data):
			if self.get_song_by_id(data['Id']) is not None:
					return abort(409, 'A song with the provided ID already exists.')
			try:
				song_context = SongContext(**data)
				db.session.add(song_context)
				db.session.commit()
				return song_context
			except Exception as e:
				return abort(400, e)
		
		def create_songs(self, data_list):
			created_songs = [db.session.add(SongContext(**data)) for data in data_list]
			db.session.commit()
			return created_songs

		def get_all_songs(self):
			song_context = SongContext.query.all()
			return song_context

		def get_song_by_id(self, id: int):
			song_context = SongContext.query.get(id)
			return song_context
		
		def update_song(self, id: int, data):
			song_context = SongContext.query.get(id)
			print(song_context)
			if(song_context is not None):
				song_context.update(db, data)
			return song_context

		def delete_song(self, id: int):
			song_context = SongContext.query.get(id)
			if(song_context is not None):
				song_context.delete(db)
			return song_context
		
		def search_songs_by_genre(self, genre):
				songs = SongContext.query.filter_by(Genre=genre).all()
				return songs
		