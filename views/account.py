import json
import jsonschema
from datetime import datetime
from django.db import connection
from django.core import serializers
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password, check_password
from models.models import Customer, Driver


@require_http_methods(["POST"])
def create_account(request: HttpRequest):
    payload = json.loads(request.body)
    # Import the Customer model

    if payload["account_type"] == "customer":
        # Create a new customer object
        new_customer = Customer(
            email=payload["email"],
            password=make_password(payload["password"]),
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            address_line_one=payload["address_line_one"],
            city=payload["city"],
            state=payload["state"],
            zipcode=int(payload["zipcode"]),
            card_number=int(payload["card_number"]),
            name_on_card=payload["name_on_card"],
            expiration_date=payload["expiration_date"],
        )
        # Save the customer to the database
        new_customer.save()
    else:
        new_driver = Driver(
            email=payload["email"],
            password=make_password(payload["password"]),
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            phone_number=payload["phone_number"],
            vehicle_type=payload["vehicle_type"],
            license_number=payload["license_number"],
            year=payload["year"],
            make = payload["make"],
            model=payload["model"]
        )
        new_driver.save()
        
@require_http_methods(["POST"])
def authenticate(request: HttpRequest):
    payload = json.loads(request.body)
    email = payload["email"]
    if payload["account_type"] == "customer":
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return HttpResponse("Invalid email or password", status=401)

        if check_password(payload["password"], customer.password):
            return HttpResponse("Authenticated", status=200)
        else:
            return HttpResponse("Invalid email or password", status=401)
    else:
        try:
            driver = Driver.objects.get(email=email)
        except Driver.DoesNotExist:
            return HttpResponse("Invalid email or password", status=401)

        if check_password(payload["password"], driver.password):
            return HttpResponse("Authenticated", status=200)
        else:
            return HttpResponse("Invalid email or password", status=401)

        
 
    
