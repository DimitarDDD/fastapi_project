from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:pass123pass@localhost:5432/databreathe"
engine=create_engine(DATABASE_URL, echo=True)

SessionLocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base=declarative_base()

