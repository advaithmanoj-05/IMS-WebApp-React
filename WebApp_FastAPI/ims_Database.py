from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DataBase = "mysql+pymysql://root:Sa121243@localhost:3306/stockmanagementsystem"
#auth_plugin='mysql_native_password'
engine = create_engine(URL_DataBase)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

