from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
# URL for MySQL: mysql+pymysql://{user}:{password}@{host}:3306/tododb
database_url = os.environ.get("DATABASE_URL", "sqlite:///./todo.db")


engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
