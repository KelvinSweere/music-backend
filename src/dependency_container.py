from dependency_injector import containers, providers

from src.infrastructure import ArtistContextService
from src.infrastructure import SongContextService


def setup_dependency_container(app, modules=None, packages=None):
    container = DependencyContainer()
    app.container = container
    app.container.wire(modules=modules, packages=packages)
    return app


class DependencyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration()
    artist_context_service = providers.Factory(ArtistContextService)
    song_context_service = providers.Factory(SongContextService)
