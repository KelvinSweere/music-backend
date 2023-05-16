import logging

from dependency_injector.wiring import inject, Provide
from flask import Blueprint, request

from src.api.responses import create_response
from src.api.schemas import ArtistContextSchema
from src.dependency_container import DependencyContainer

logger = logging.getLogger(__name__)
blueprint = Blueprint('artist_context', __name__)


@blueprint.route('/artist', methods=['POST'])
@inject
def create_artist(
    artist_context_service=Provide[
        DependencyContainer.artist_context_service
    ]
):
    artist_data = request.get_json(force=True) 
    result = artist_context_service.create_artist(artist_data)
    return create_response(result, ArtistContextSchema)


@blueprint.route('/artist', methods=['GET'])
@inject
def get_all_artists(
    artist_context_service=Provide[
        DependencyContainer.artist_context_service
    ]
):
    result = artist_context_service.get_all_artists()
    return create_response(result, ArtistContextSchema(many=True))


@blueprint.route('/artist/<int:id>', methods=['GET'])
@inject
def get_artist_by_id(
    id,
    artist_context_service=Provide[
        DependencyContainer.artist_context_service
    ]
):
    result = artist_context_service.get_artist_by_id(id)
    return create_response(result, ArtistContextSchema)


@blueprint.route('/artist/<int:id>', methods=['PUT'])
@inject
def update_artist(
    id,
    artist_context_service=Provide[
        DependencyContainer.artist_context_service
    ]
):
    artist_data = request.json
    result = artist_context_service.update_artist(id, artist_data)
    return create_response(result, ArtistContextSchema)


@blueprint.route('/artist/<int:id>', methods=['DELETE'])
@inject
def delete_artist(
    id,
    artist_context_service=Provide[
        DependencyContainer.artist_context_service
    ]
):
    result = artist_context_service.delete_artist(id)
    return create_response(result, ArtistContextSchema)
