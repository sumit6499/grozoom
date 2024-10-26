from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

try:
    DATABASE_URI=os.getenv("DATABASE_URI")
except :
    print("database env not configured")

try:
    engine=create_engine(DATABASE_URI)
    SessionLocal =sessionmaker(autoflush=False,bind=engine)
except :
    print("sql db config fail")