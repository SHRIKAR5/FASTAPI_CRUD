from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB

# URL_DATABASE = 'mysql+pymysql://root:root@localhost:3306/employeemanagement'
URL_DATABASE = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


