# Build a REST API with FastAPI, PostgreSQL and SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 



### Setting up the database

* Install PostgreSQL and create your user and database

* Change this line in ` database.py ` to 

``` 
engine=create_engine("postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
    echo=True
)
```

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

### Create the database
``` python create_db.py ```

## Run the API
``` uvicorn main:app --reload ```  
test the the url path with execute button

# go to the browser  

``` http://127.0.0.1:8000/docs ``` 


