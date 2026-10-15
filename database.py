from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

URL = "mysql+pymysql://root:123456!@localhost:3306/phone_store_db"
engine = create_engine(URL)

sessionLocal = sessionmaker(autoflush= False, bind= engine, expire_on_commit=False)
Base = declarative_base()
def get_db():
    db = sessionLocal()
    try :
        yield db
    finally:
        db.close()        
    