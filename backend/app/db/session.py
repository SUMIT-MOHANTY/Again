from backend.app.config import settings

if settings.use_mock:
    from backend.app.services.mock_postgres import MockPostgres
    engine = MockPostgres()
else:
    from sqlalchemy import create_engine
    engine = create_engine(settings.POSTGRES_URI, echo=False)

def get_engine():
    return engine
