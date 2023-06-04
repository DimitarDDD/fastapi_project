from pydantic import BaseModel
import datetime

class Customer(BaseModel):
    customer_id: int
    home_store = str
    customer_first_name: str
    customer_email: str 
    customer_since: str 
    loyalty_card_number: str 
    birthdate: str  
    gender: str
    birth_year: int

    class Config:
        orm_mode = True

class Product(BaseModel): 
    product_id: int
    product_group = str
    product_category: str
    product_type: str 
    product: str 
    product_description: str 
    unit_of_measure: str  
    current_wholesale_pricer: float
    current_retail_price: str 
    tax_exempt_yn: str 
    promo_yn: str 
    new_product_yn: str


    class Config:
        orm_mode = True
        


class SalesOutlet(BaseModel): 
    sales_outlet_id  =int
    sales_outlet_type = str  
    store_square_feet = int   
    store_address = str    
    store_city = str   
    store_state = str    
    store_telephone = str   
    store_postal_code = int
    store_longitude = str  
    store_latitude= float   
    manager= str  
    neighorhood =str
     

class PastryInventory(BaseModel): 
    sales_outled_id = int
    transaction_date = str  
    product_id = int
    quantity_sold = int
    waste =  int
    wasteprocent = str
    

class SalesReceipt(BaseModel): 
    id = int 
    transaction_id =  int
    transaction_date = str
    transaction_time = str 
    sales_outlet_id = int
    staff_id = int
    customer_id = int
    instore_yn = str  
    order = int
    line_item_id = int
    product_id = int
    quantity = int
    line_item_amount = float
    unit_price =  float
    promo_item_yn = str


class Staff(BaseModel): 
    staff_id =  int
    first_name = str
    last_name = str
    position = str 
    start_date = str

    
