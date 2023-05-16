import logging

from dependency_injector.wiring import inject, Provide
from flask import Blueprint

from src.api.responses import create_response
from src.api.schemas import ArtistContextSchema
from src.dependency_container import DependencyContainer

logger = logging.getLogger(__name__)
blueprint = Blueprint('artist_context', __name__)

@blueprint.route('/artist/<int:id>', methods=['GET'])
@inject
def get_artist(
    id,
    artist_context_service=Provide[
        DependencyContainer.artist_context_service
    ]
):
    result = artist_context_service.get_service_context(id)
    return create_response(result, ArtistContextSchema)