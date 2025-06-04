from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔁 Replace these values with your actual MySQL config:
USERNAME = "root"
PASSWORD = "1234"
HOST = "localhost"
DB_NAME = "fastapi_users"

DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
