# Testing the API for WebMain of IMS ver1 (IN PROG)


# IMPORTS
from fastapi import FastAPI,HTTPException,Depends,status
from sqlalchemy import text
import ims_Models
from ims_Database import engine,SessionLocal
from pydantic import BaseModel
from typing import Annotated,List
from sqlalchemy.orm import Session
from random import randrange
from datetime import datetime,date
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import cryptography
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


ims_Models.Base.metadata.create_all(bind=engine)
numeric='1234567890'
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def genCode():
    itemId=''
    for i in range(0,3):
        randno=randrange(0,(len(numeric)-1))
        itemId=itemId+str(numeric[randno])
    randno=randrange(0,(len(alpha)-1))
    itemId=itemId+'-'+str(alpha[randno])
    return itemId
    # print("generated: "+itemId)
    # setph(itemId,0)

db_dependency= Annotated[Session,Depends(get_db)]

# if get_db():
#     print("yes")
# else:
#     print("nope")
class StocksBase(BaseModel):
    item_id:str
    name:str
    price:str
    quantity:str
    category:str
    date:date

class StocksModel(StocksBase):
    id:int

# @app.get("/")
# async def root():
#     return {"Message":"Hello World"}

@app.get("/stocks/get_stocks/",status_code=status.HTTP_200_OK)
async def get_stocks(db:db_dependency,skip:int=0,limit:int=100):
    #current_stocks= db.query(ims_Models.Stocks).all()
    current_stocks=db.query(ims_Models.Stocks).offset(skip).limit(limit).all()
    if current_stocks is None:
       HTTPException(status_code=404,detail="Stocks are empty!")
    return current_stocks

# @app.get("/stocks/search_stocks/",status_code=status.HTTP_200_OK)
# async def search_stocks(db:db_dependency,sitemId:Optional[str]=None,sname:Optional[str]=None,scategory:Optional[str]=None):
#     if sitemId is None:
#         if sname is None:
#             if scategory is None:
#                 HTTPException(status_code=404, detail="No fields applied")
#             else:
#                 Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.category == scategory).all()
#                 if Item is None:
#                     HTTPException(status_code=404, detail="Item not found")
#                 return Item
#         else:
#             Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.name == sname).all()
#             if Item is None:
#                 HTTPException(status_code=404, detail="Item not found")
#             return Item
#     else:
#         Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id == sitemId).all()
#         if Item is None:
#             HTTPException(status_code=404, detail="Item not found")
#         return Item



# @app.post("/stocks/add_stocks/",status_code=status.HTTP_201_CREATED)
# async def add_to_stocks(new_stock:StocksBase,db:db_dependency):
#     new_stock=ims_Models.Stocks(**new_stock.model_dump())
#     flag=0
#     while True:
#         chker = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id == new_stock.item_id).first()
#         if chker is None:
#             db.add(new_stock)
#             db.commit()
#             break
#         else:
#             new_stock.item_id =genCode()
#             flag=1
#     if flag==1:
#         return f"Code already exists changed to {new_stock.item_id}"
#     else:
#         return f"This is still -  {new_stock.item_id}"
    
@app.post("/stocks/add_stocks/",status_code=status.HTTP_201_CREATED,response_model=StocksModel)
async def add_to_stocks(new_stock:StocksBase,db:db_dependency):
    db_new_stock=ims_Models.Stocks(**new_stock.dict())
    db.add(db_new_stock)
    db.commit()
    db.refresh(db_new_stock)
    return db_new_stock

# @app.delete("/stocks/del_stocks/{itemId}/",status_code=status.HTTP_200_OK)
# async def del_stocks(itemId:str ,db: db_dependency):
#     Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id==itemId).first()
#     if Item is None:
#         HTTPException(status_code=404,detail="Item not found")
#     db.delete(Item)
#     db.commit()


# @app.put("/stocks/edit_stocks/{item_Id}/",status_code=status.HTTP_200_OK)
# async def edit_stocks(db:db_dependency,itemId:str,sname:Optional[str]=None,scategory:Optional[str]=None,squantity:Optional[str]=None,sprice:Optional[str]=None):
#     Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id == itemId).first()
#     if Item is None:
#         HTTPException(status_code=404, detail="Item not found")
#     if sname is None:
#         if scategory is None:
#             if squantity is None:
#                 if sprice is None:
#                     HTTPException(status_code=404, detail="No fields applied")
#                 else:
#                     Item.price=sprice
#                     return f"Price of Item Code:{itemId} has been updated to {sprice}",Item
#             else:
#                 Item.quantity = squantity
#                 return f"Quantity of Item Code:{itemId} has been updated to {squantity}", Item
#         else:
#             Item.category = scategory
#             return f"Category of Item Code:{itemId} has been updated to {scategory}", Item
#     else:
#         Item.name = sname
#         return f"Name of Item Code:{itemId} has been updated to {sname}", Item

#
#
# @app.put("/stocks/edit_name/{itemId}",status_code=status.HTTP_200_OK)
# async def edit_name(itemId:str,new_n:str,db:db_dependency):
#     Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id == itemId).first()
#     if Item is None:
#         HTTPException(status_code=404, detail="Item not found")
#     Item.name = new_n
#     db.commit()
#     return "rows 1 has been affected"
#
# @app.put("/stocks/edit_price/{itemId}",status_code=status.HTTP_200_OK)
# async def edit_price(itemId:str,new_p:int,db:db_dependency):
#     Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id == itemId).first()
#     if Item is None:
#         HTTPException(status_code=404, detail="Item not found")
#     Item.price = new_p
#     db.commit()
#     return "rows 1 has been affected"
#
# @app.put("/stocks/edit_quantity/{itemId}",status_code=status.HTTP_200_OK)
# async def edit_quantity(itemId:str,new_q:int,db:db_dependency):
#     Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id == itemId).first()
#     if Item is None:
#         HTTPException(status_code=404, detail="Item not found")
#     Item.quantity = new_q
#     db.commit()
#     return "rows 1 has been affected"
#
# @app.put("/stocks/edit_category/{itemId}",status_code=status.HTTP_200_OK)
# async def edit_category(itemId:str,new_c:str,db:db_dependency):
#     Item = db.query(ims_Models.Stocks).filter(ims_Models.Stocks.item_id == itemId).first()
#     if Item is None:
#         HTTPException(status_code=404, detail="Item not found")
#     Item.category = new_c
#     db.commit()
#     return "rows 1 has been affected"



