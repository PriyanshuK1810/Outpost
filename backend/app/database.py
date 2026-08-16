from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_engine = create_engine("sqlite:///./dev.db")
local_session = sessionmaker(bind=database_engine)
db_base = declarative_base()
