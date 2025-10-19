from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base
from .utils import get_db_path, is_create_db, logger

engine = create_engine(get_db_path(), echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def setup_database() -> None:
    if not is_create_db():
        Base.metadata.create_all(engine)
        tables = list(Base.metadata.tables.keys())
        logger.info(f"New tables created: %s", tables)
    else:
        logger.debug("Tables already exist")