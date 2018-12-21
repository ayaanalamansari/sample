from django.db import models


class Currency(models.Model):
    """
    This table stores the master data about currencies.
    """
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)

    def __str__(self):
        """Return str for object."""
        return "{name}".format(
            name=self.name,
        )


class Country(models.Model):
    """
    This table stores the master data about countries
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, null=True)
    phone_code = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        """Return str for object."""
        return "{name}".format(
            name=self.name,
        )


class State(models.Model):
    """
    This table stores the master data about states
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        """Return str for object."""
        return "{name}> {country}".format(
            name=self.name,
            country=self.country,
        )

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

    def __str__(self):
        """Return str for object."""
        return "{city_name}> {state}".format(
            city_name=self.city_name,
            state=self.state,
        )


class Timezone(models.Model):
    """
    This table stores the master data about timezones
    """
    display_name = models.CharField(max_length=100)
    day_light_name = models.CharField(max_length=100, null=True)
    base_utc_offset = models.DecimalField(max_digits=20, decimal_places=5)
    standard_name = models.CharField(max_length=100, null=True)
    supports_day_light_saving_time = models.BooleanField(default=False)
