from models import error_logs

from db.session import engine


def init_db() -> None:
    error_logs.Base.metadata.create_all(bind=engine)
