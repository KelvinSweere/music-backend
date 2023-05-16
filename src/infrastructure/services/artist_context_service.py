from src.infrastructure.models.artist_context import ArtistContext
from src.infrastructure.databases import sqlalchemy_db as db

class ArtistContextService:

    def get_service_context(self, id: int):
        status = ArtistContext.query.first()

        if status is None:
            status = ArtistContext()
            status.save(db)

        return status