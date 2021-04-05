from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
db = os.getenv('postgres_db')
db_host = os.getenv('postgres_host')
db_port = os.getenv('postgres_port')
db_user = os.getenv('postgres_user')
db_password = os.getenv('postgres_password')
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db}", echo=True)
meta = MetaData()
Base = declarative_base()