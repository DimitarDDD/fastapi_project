from fastapi.testclient import TestClient  
from main import app  
from fastapi import status

client= TestClient(app=app) 


def test_birthday():
    response = client.get('/customer/birthday') 
    assert response.status_code == status.HTTP_200_OK 
    assert response.json() == {
    "customers": [
    {
      "customer_id": 54,
      "customer_first_name": "Ferris Kidd"
    },
    {
      "customer_id": 248,
      "customer_first_name": "Fritz Washington"
    },
    {
      "customer_id": 372,
      "customer_first_name": "Leigh William"
    },
    {
      "customer_id": 718,
      "customer_first_name": "Cole Thompson"
    },
    {
      "customer_id": 5070,
      "customer_first_name": "Mallory"
    },
    {
      "customer_id": 8189,
      "customer_first_name": "Irene"
    },
    {
      "customer_id": 8499,
      "customer_first_name": "Clementine"
    }
  ]
    }
     

def test_sales():
    response = client.get('/products/top-selling-products/2019') 
    assert response.status_code == status.HTTP_200_OK 
    assert response.json() == {
        "products": [
        {
        "product_name": "Earl Grey Rg",
        "total_sales": 1558
        },
        {
        "product_name": "Dark chocolate Lg",
        "total_sales": 1546
        },
        {
        "product_name": "Latte",
        "total_sales": 1531
        },
        {
        "product_name": "Morning Sunrise Chai Rg",
        "total_sales": 1513
        },
        {
        "product_name": "Ethiopia Rg",
        "total_sales": 1506
        },
        {
        "product_name": "Columbian Medium Roast Rg",
        "total_sales": 1502
        },
        {
        "product_name": "Serenity Green Tea Rg",
        "total_sales": 1498
        },
        {
        "product_name": "Peppermint Rg",
        "total_sales": 1498
        },
        {
        "product_name": "Traditional Blend Chai Rg",
        "total_sales": 1497
        },
        {
        "product_name": "Sustainably Grown Organic Lg",
        "total_sales": 1496
        }
      ]
    }
    

def test_last_order():
    response = client.get('/customer/birthday') 
    assert response.status_code == status.HTTP_200_OK 
   