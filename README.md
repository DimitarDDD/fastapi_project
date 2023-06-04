# Build a REST API with FastAPI, PostgreSQL and SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface.  
This app has three endpoints giving the needed data 
/customers/birthday
Response:
{
"customers": [
{
"customer_id": 12345
"customer_first_name": "Joe Doe"
},
]
}

Endpoint: /products/top-selling-products/{year}
Response:
{
"products: [
{
"product_name: "Espresso Roast",
"total_sales": 12345
},
]
}

Endpoint: /customers/last-order-per-customer
Response:
{
"customers": [
{
"customer_id": 12345,
"customer_email": "yyyyy@zzzzz.xx",
"last_order_date": "2023-01-01"
},
]
}

### Setting up the database

* Install PostgreSQL and create your user and database

* Change this line in ` database.py ` to 

``` 
engine=create_engine("postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
    echo=True
)
```
* Insert wanted data from a csv file using with pgadmin4 insert/export functionality or with using a sql query

### Create a virtual environment
This can be done with 
``` python -m venv env ```

activate the virtual environment with 

``` 
env/bin/activate
```

or 

```
env\Scripts\activate
```

### Install the requirements 

``` 
pip install -r requirements.txt
```

## use alembic if needed 
```  alembic init alembic ```
``` alembic revision --autogenerate -m ```

## Run the API
``` uvicorn main:app --reload ```  
test the url paths from swager ui pressing execute button and adding query parameter in the url if it is needed

# go to the browser  

``` http://127.0.0.1:8000/docs ``` 


