from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text, DateTime, Float, ForeignKey

class Customer(Base):
    __tablename__ = 'customers'
    customer_id  = Column(Integer, primary_key=True, index=True) 
    home_store =  Column(Integer) 
    customer_first_name = Column(String) 
    customer_email = Column(String) 
    customer_since = Column(DateTime(timezone=True)) 
    loyalty_card_number = Column(String) 
    birthdate = Column(DateTime(timezone=True))  
    gender = Column(String)  
    birth_year = Column(Integer)



class Product(Base):
    __tablename__ = 'products' 
    product_id  = Column(Integer, primary_key=True, index=True)  
    product_group = Column(String)  
    product_category = Column(String)   
    product_type = Column(String)    
    product = Column(String)     
    product_description = Column(String)     
    unit_of_measure = Column(String)      
    current_wholesale_price = Column(Float)  
    current_retail_price = Column(String)  
    tax_exempt_yn = Column(String)   
    promo_yn = Column(String)  
    new_product_yn = Column(String)  
    

class SalesOutlet(Base): 
    __tablename__ = 'salesoutlet'  
    sales_outlet_id  = Column(Integer, primary_key=True, index=True)  
    sales_outlet_type = Column(String)  
    store_square_feet = Column(Integer)   
    store_address = Column(String)    
    store_city = Column(String)     
    store_state = Column(String)     
    store_telephone = Column(String)      
    store_postal_code = Column(Integer)  
    store_longitude = Column(String)  
    store_latitude= Column(Float)   
    manager= Column(String)  
    neighorhood = Column(String)  
     

class PastryInventory(Base): 
    __tablename__ = 'pastryinventory'   
    id = Column(Integer, primary_key=True, index=True)  
    sales_outled_id = Column(Integer, ForeignKey("salesoutlet.sales_outlet_id", ondelete='CASCADE'), nullable=False)
    transaction_date = Column(DateTime(timezone=True))   
    product_id =  Column(Integer, ForeignKey("products.product_id", ondelete='CASCADE'), nullable=False)
    start_of_day  = Column(Integer) 
    quantity_sold =  Column(Integer)  
    waste =  Column(Integer)  
    wasteprocent = Column(String)  
    

class SalesReceipt(Base): 
    __tablename__ = 'salesreceipts'     
    id = Column(Integer, primary_key=True, index=True)  
    transaction_id =  Column(Integer) 
    transaction_date = Column(DateTime(timezone=True)) 
    transaction_time = Column(String)  
    sales_outlet_id = Column(Integer, ForeignKey("salesoutlet.sales_outlet_id", ondelete='CASCADE'), nullable=False)
    staff_id = Column(Integer, ForeignKey("staff.staff_id", ondelete='CASCADE'), nullable=False)
    customer_id = Column(Integer)
    instore_yn = Column(String)  
    order = Column(Integer)  
    line_item_id = Column(Integer) 
    product_id = Column(Integer, ForeignKey("products.product_id", ondelete='CASCADE'), nullable=False)
    quantity =   Column(Integer)
    line_item_amount =  Column(Float)
    unit_price =  Column(Float)
    promo_item_yn = Column(String)


class Staff(Base): 
    __tablename__ = 'staff' 
    staff_id =  Column(Integer, primary_key=True, index=True)  
    first_name = Column(String) 
    last_name = Column(String)  
    position = Column(String)  
    start_date = Column(DateTime(timezone=True))  
    location = Column(String)     

    
