from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
#database_url = os.environ.get("DATABASE_URL", "sqlite:///./todo.db")
database_url = os.environ.get("DATABASE_URL", "mysql+pymysql://admin:password@db:3306/tododb'")

engine = create_engine(database_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
 
