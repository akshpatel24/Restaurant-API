from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SECRET_KEY = "Aksh's world"  # Replace with a secure secret key
ALGORITHM = "HS256"
# Database connection parameters
server = 'DESKTOP-9DHBJDE'
database = 'master'
username = 'sa'
password = 'Hello012345678910!'
connection_url = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_url, echo=True) #if true then and then debugging will occur.
# Define declarative base
Base = declarative_base()

# Define session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
