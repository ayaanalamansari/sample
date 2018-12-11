from django.db import models


class Currency(models.Model):
    """
    This table stores the master data about currencies.
    """
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)


class Country(models.Model):
    """
    This table stores the master data about countries
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, null=True)
    phone_code = models.DecimalField(max_digits=5, decimal_places=0)

class State(models.Model):
    """
    This table stores the master data about states
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    """
    This table stores the master data about cities
    """
    city_name = models.CharField(max_length=100)
    city_name_rc = models.CharField(max_length=100, null=True)
    city_name_caps = models.CharField(max_length=100, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)

class Address(models.Model):
    """
    This table stores the master data about address of user type entity or company
    """
    address_line1 = models.CharField(max_length=150)
    address_line2 = models.CharField(max_length=150, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

class Timezone(models.Model):
    """
    This table stores the master data about timezones
    """
    display_name = models.CharField(max_length=100)
    day_light_name = models.CharField(max_length=100, null=True)
    base_utc_offset = models.DecimalField(max_digits=20, decimal_places=5)
    standard_name = models.CharField(max_length=100, null=True)
    supports_day_light_saving_time = models.BooleanField(default=False)
