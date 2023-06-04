import uvicorn
import models
from sqlalchemy.orm import Session , Query
from fastapi import FastAPI
from schemas import Customer as SchemaCustomer
from schemas import SalesReceipt as SchemaSalesReceipt
#from router import router
from schemas import Customer
from fastapi_sqlalchemy import DBSessionMiddleware, db
from models import Product as ModelProduct
from models import Customer as ModelCustomer
from database import engine
from fastapi.encoders import jsonable_encoder  
from fastapi.responses import JSONResponse, Response
import operator
from collections import defaultdict
import itertools  
from datetime import datetime as dt
from logic import *

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:pass123pass@localhost:5432/databreathe")




"""summary -  function retunrs if the customers who are visiting the shop has a birthday today
    Returns:_	
    Response body
   {
    "customers": [
    {
      "customer_id": 54,
      "customer_first_name": "Ferris Kidd"
    },
    {
      "customer_id": 248,
      "customer_first_name": "Fritz Washington"
    },
"""


@app.get('/customer/birthday', response_model=SchemaCustomer, name='Birthday customers', description= 'Customers who has a birthday today')
async def birthday():  
    final = {}
    new = []
    birthday_customers = db.session.query(models.Customer).all()  
    # fromating the query object to json object
    json_data = jsonable_encoder(birthday_customers) 
    for el in json_data: 
        z = str(dt.now())[5:10] 
        if el['birthdate'][5:10] == z: 
            newdict = {}   
            newdict['customer_id'] = el['customer_id'] 
            newdict['customer_first_name'] = el['customer_first_name']  
            new.append(newdict) 
            
    final['customers']=new
        
    return JSONResponse(content=final)


"""summary - the function is working only with year 2019 because of the data in the db and it returns a  the top 10 products
    Returns:_	
    Response body
    {
    "products": [
        {
        "product_name": "Earl Grey Rg",
        "total_sales": 1558
        }, 
    }
"""
@app.get('/products/top-selling-products/{year}', response_model=SchemaSalesReceipt, name='Top 10 products', description= 'The top 10 selling products for a specific year.')
async def sales(year:str):
    final = {}  
    check = {} 
    sales = db.session.query(models.SalesReceipt).all()  
    # fromating the query object to json object
    json_data = jsonable_encoder(sales)     
    for el in json_data:  
        data = el['transaction_date'][0:4]  
        if data == year:
            prod_id = el['product_id']   
            prod_quant = el['quantity']   
            if prod_id not in check:  
                check[prod_id] = prod_quant
            else: 
                p = check[prod_id] 
                p += prod_quant
                check[prod_id] = p  
        else: 
            return Response("the year chosen is not in the databse")
             
    dict2 = {}
    for i in check:
        product1 = db.session.query(models.Product).get(i) 
        # fromating the query object to json object
        json_data = jsonable_encoder(product1)    
        product = json_data['product']        
        dict2[product] = check[i]
    
    customer_list = []
    sorted_products_by_sales = sorted(dict2.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_products_by_sales)  
    # slicing the sorted dict to get top 10
    sliced_converted_dict = dict(itertools.islice(converted_dict.items(), 10))   
    for i in sliced_converted_dict:
        res = dict() 
        res["product_name"] = i
        res["total_sales"] = sliced_converted_dict[i]
        customer_list.append(res)
    
    final['products']=customer_list
   
    return JSONResponse(content=final) 


"""summary - the function is returning which is the last order per customer email didnt worked out in the end
    Returns:_	
   Response:
    {
       "customers": [
        {
        "customer_id": 12345,
        "last_order_date": "2023-01-01"
        },
        ]
    }
"""

@app.get('/customers/last-order-per-customer', response_model=SchemaSalesReceipt, name='The last order per customer ', description= 'The last order per customer ')
async def last_order():   
    new = []
    final = {}  
    all_customers = []
    sales = db.session.query(models.SalesReceipt).all() 
    json_data = jsonable_encoder(sales)     
    for el in json_data:   
        cus = el['customer_id']  
        # filtering the customers id
        if cus not in all_customers and cus != '0':
            all_customers.append(cus)
    
    new_dict = {}
    for el in json_data: 
        cus = el['customer_id'] 
        if cus in all_customers:    
            # slicing transaction date
            transaction_date = el['transaction_date'][:10] 
            transaction_time = el['transaction_time']
            datitime_format_st = transaction_date +" "+ transaction_time   
            if cus not in new_dict:
                new_dict[cus]= [] 
                new_dict[cus].append(datitime_format_st)
            else:
                new_dict[cus].append(datitime_format_st)
    
    # copy the dict  
    new_dict2= new_dict.copy()
    for i in new_dict2:    
        # getting the nearest date from datime.now  the function is in logic.py
        nearest_date = nearest(new_dict2[i])   
        new_dict2[i] = str(nearest_date)[:10]
    
    for j in new_dict2:  
       
        res = dict() 
        res["customer_id"] = j 
        #book2 = db.session.query(models.Customer).get(k)
        #json_data1 = jsonable_encoder(book2)
        #p = str(json_data1['customer_email']) 
        #res['customer_email'] = json_data1['customer_email'] 
        res["last_order_date"] = new_dict2[j] 

        new.append(res)
        
    final['customers']=new
    

    return JSONResponse(content=final) 