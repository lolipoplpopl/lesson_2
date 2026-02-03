import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DB_URL = "postgresql://postgres:12@localhost:5432/lesson9_haha"


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()
    Base.metadata.drop_all(engine)
