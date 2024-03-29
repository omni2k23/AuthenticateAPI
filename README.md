# AuthenticateAPI

An API to create `User` and `Driver` accounts and authenticate them.

## Install

Before running the service, make sure you have the dependecies to run it. You can run this command:
`pip install djangorestframework markdown django-filter psycopg2 python-environ`
```
DB_NAME=dbname
DB_USER=user
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port
```

## Run the app
`python manage.py runserver 0.0.0.0:8000`

# REST API
To create a customer send a POST request to `createAccount/`. Your post request should be like this 
```
{
  "account_type": "customer",
  "email": "johndoe@example.com",
  "password": "mypassword",
  "first_name": "John",
  "last_name": "Doe",
  "address_line_one": "123 Main St",
  "city": "Anytown",
  "state": "CA",
  "zipcode": "12345",
  "card_number": "1234567890123456",
  "name_on_card": "John Doe",
  "expiration_date": "2023-05-31"
}
```

To create a driver, send a POST request to `createAccount/`. Your post request should be like this.
```
{
  "account_type": "driver",
  "email": "janedoe@example.com",
  "password": "mypassword",
  "first_name": "Jane",
  "last_name": "Doe",
  "phone_number": "123-456-7890",
  "vehicle_type": "sedan",
  "license_number": "AB123456",
  "year": "2018",
  "make": "Toyota",
  "model": "Camry"
}
``` 

To authenticate the user, send a POST request to `authenticate/`. Your post request should be like this.
```
{
    "email": "",
    "password: ""
}
```