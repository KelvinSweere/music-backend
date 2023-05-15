from .service_context import blueprint as service_context_blueprint

def setup_blueprints(app) -> None:
    app.register_blueprint(service_context_blueprint, url_prefix="/api")
    return app


__all__ = ['setup_blueprints']
