
# Django Backend - OnlineShopping App

This is a online shopping application which backend is developed with Django & Django rest-framework for api calls.

## URL
https://djangoprojectworks.onrender.com/api/

### Update:
In coming release will provide admin access credentials to use this site for testing other than GET options. For now only GET method is only applicable to used.

## Users:

### 1. Get list of users:
#### URL: 
https://djangoprojectworks.onrender.com/api/user/

#### Description: 
You will get list of Users who created account in the application in below format.

#### Allowed methods: 
GET, POST, HEAD

#### Example:

[

    {
        "name": "Usertest1",
        "email": "usertest1@mail.com",
        "phone": null,
        "gender": null,
        "is_active": true,
        "is_staff": false,
        "is_superuser": false
    } ,
    {
        "name": "Usertest2",
        "email": "usertest2@mail.com",
        "phone": null,
        "gender": null,
        "is_active": true,
        "is_staff": false,
        "is_superuser": false
    }
]

### 2. Get specific User details using Id:

#### URL: 
https://djangoprojectworks.onrender.com/api/user/2/

#### Description:
You will get User specific information using Id after user/{ID} in json format.

#### Allowed methods: 
GET, PUT, PATCH, DELETE, HEAD

#### Example:

##### {
    "name": "Usertest1",
    "email": "usertest1@mail.com",
    "phone": null,
    "gender": null,
    "is_active": true,
    "is_staff": false,
    "is_superuser": false
##### }

## Products:

### 1. Get list of Products:
#### URL:
https://djangoprojectworks.onrender.com/api/products/

#### Description:
You will get list of products information available in added in application

#### Allowed methods: 
GET, POST, HEAD - only Admin can use POST.

#### Example:

##### [
    {
        "id": 1,
        "name": "RRR Tshirt",
        "description": "Hoodie for movie lovers",
        "price": "10",
        "image": "https://djangoprojectworks.onrender.com/media/images/rrr-tshirt_hujI3F6.jpg",
        "category": "https://djangoprojectworks.onrender.com/api/category/1/",
        "stock": "20",
        "is_active": true
    },
    {
        "id": 2,
        "name": "Black Tshirt",
        "description": "Tshirt for coders",
        "price": "15",
        "image": "https://djangoprojectworks.onrender.com/media/images/black-tshirt_RqXjF0y.jpg",
        "category": "https://djangoprojectworks.onrender.com/api/category/2/",
        "stock": "10",
        "is_active": true
    },
    {
        "id": 3,
        "name": "Blue Tshirt",
        "description": "Oversized Tshirt",
        "price": "14",
        "image": "https://djangoprojectworks.onrender.com/media/images/chex-tshirt_pxv8sh9.jpg",
        "category": "https://djangoprojectworks.onrender.com/api/category/3/",
        "stock": "15",
        "is_active": true
    },
    {
        "id": 4,
        "name": "Tshirt",
        "description": "Tshirt information",
        "price": "30",
        "image": "https://djangoprojectworks.onrender.com/media/images/pexels-sebastiaan-stam-1311590.jpg",
        "category": "https://djangoprojectworks.onrender.com/api/category/1/",
        "stock": "10",
        "is_active": true
    }
##### ]

### 2. Get specific product information:
#### URL:
https://djangoprojectworks.onrender.com/api/products/1/

#### Description:
You will get product specific information in json format.
#### Allowed methods: 
GET, PUT, PATCH, DELETE, HEAD - only Admin can use POST, PUT, DELETE.

#### Example:
##### {
    "id": 1,
    "name": "RRR Tshirt",
    "description": "Hoodie for movie lovers",
    "price": "10",
    "image": "https://djangoprojectworks.onrender.com/media/images/rrr-tshirt_hujI3F6.jpg",
    "category": "https://djangoprojectworks.onrender.com/api/category/1/",
    "stock": "20",
    "is_active": true
##### }



