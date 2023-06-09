from .artist_context import blueprint as artist_context_blueprint
from .song_context import blueprint as song_context_blueprint

def setup_blueprints(app) -> None:
    app.register_blueprint(artist_context_blueprint, url_prefix="/api")
    app.register_blueprint(song_context_blueprint, url_prefix="/api")
    return app


__all__ = ['setup_blueprints']
