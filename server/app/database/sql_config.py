from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.models.models import Base

engine = None
session_maker = None

def connect_to_mysql():
    global engine, session_maker
    engine = create_engine(
        f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}/{settings.MYSQL_DB}")
    session_maker = sessionmaker(bind=engine)

def close_mysql_connection():
    global engine
    if engine:
        engine.dispose()

def get_mysql_session():
    global session_maker
    return session_maker()