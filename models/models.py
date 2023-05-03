from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    email = models.TextField()
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    address_line_one = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.IntegerField()
    card_number = models.IntegerField()
    name_on_card = models.TextField()
    expiration_date = models.DateField()

    class Meta:
        app_label = 'AuthenticateAPI'
        db_table = 'customer'


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    email = models.TextField()
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()
    vehicle_type = models.TextField()
    license_number = models.TextField()
    year = models.IntegerField()
    make = models.TextField()
    model = models.TextField()

    class Meta:
        app_label = 'AuthenticateAPI'
        db_table = 'driver'
