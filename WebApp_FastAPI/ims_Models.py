# To set the Database Tables format for the API
from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.sql.functions import current_timestamp

from ims_Database import Base

class Stocks(Base):
    __tablename__="stocks"

    id = Column(Integer,primary_key=True,index=True,nullable=False,autoincrement=True)
    item_id = Column(MEDIUMTEXT,nullable=False,unique=True)
    name = Column(MEDIUMTEXT,nullable=False)
    price = Column(MEDIUMTEXT,nullable=False)
    quantity = Column(MEDIUMTEXT,nullable=False)
    category = Column(MEDIUMTEXT,nullable=False)
    date = Column(DATETIME,nullable=False,default=current_timestamp)
    #date = Column(MEDIUMTEXT,nullable=False,default=current_timestamp)

