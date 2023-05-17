import logging

from dependency_injector.wiring import inject, Provide
from flask import Blueprint, request

from src.api.responses import create_response
from src.api.schemas import SongContextSchema
from src.dependency_container import DependencyContainer

logger = logging.getLogger(__name__)
blueprint = Blueprint('song_context_blueprint', __name__)

@blueprint.route('/song', methods=['POST'])
@inject
def create_song(
    artist_context_service=Provide[
        DependencyContainer.song_context_service
    ]
):
    song_data = request.get_json(force=True) 
    result = artist_context_service.create_song(song_data)
    print(result)
    return create_response(result, SongContextSchema)

@blueprint.route('/songs', methods=['POST'])
@inject
def create_songs(
    artist_context_service=Provide[
        DependencyContainer.song_context_service
    ]
):
    song_data = request.get_json(force=True) 
    result = artist_context_service.create_songs(song_data)
    return create_response(result, SongContextSchema)

@blueprint.route('/song/<song_id>', methods=['GET'])
@inject
def get_song_by_id(
    song_id,
		artist_context_service=Provide[
				DependencyContainer.song_context_service
		]
):
		result = artist_context_service.get_song_by_id(song_id)
		return create_response(result, SongContextSchema)

@blueprint.route('/songs', methods=['GET'])
@inject
def get_all_songs(
		artist_context_service=Provide[
				DependencyContainer.song_context_service
		]
):
		result = artist_context_service.get_all_songs()
		return create_response(result, SongContextSchema(many=True))

@blueprint.route('/song/<song_id>', methods=['PUT'])
@inject
def update_song(
		song_id,
		artist_context_service=Provide[
				DependencyContainer.song_context_service
		]
):
		song_data = request.get_json(force=True) 
		result = artist_context_service.update_song(song_id, song_data)
		return create_response(result, SongContextSchema)

@blueprint.route('/song/<song_id>', methods=['DELETE'])
@inject
def delete_song(
		song_id,
		artist_context_service=Provide[
				DependencyContainer.song_context_service
		]
):
		result = artist_context_service.delete_song(song_id)
		return create_response(result, SongContextSchema)

@blueprint.route('/song', methods=['GET'])
@inject
def seach_song_by_genre(
		artist_context_service=Provide[
				DependencyContainer.song_context_service
		]
):
		genre = request.args.get('genre')
		result = artist_context_service.search_songs_by_genre(genre)
		return create_response(result, SongContextSchema(many=True))
