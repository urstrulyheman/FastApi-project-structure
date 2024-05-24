from .session import engine
from .base import Base

def init_db():
    Base.metadata.create_all(bind=engine)
