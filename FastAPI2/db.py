from sqlalchemy import create_engine

database_url = "sqlite:///./shishir"

engine = create_engine(database_url, echo=True)