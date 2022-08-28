from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

DIGITAL_INVENTORY_DATABASE_URL = environ.get("DIGITAL_INVENTORY_DATABASE_URL")

engine = create_engine(
    DIGITAL_INVENTORY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()