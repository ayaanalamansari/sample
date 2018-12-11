from django.conf.urls import url, include
from .models import Currency, Country, State, City, Timezone
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class CurrencySerializer(serializers.ModelSerializer):
    """
    Serializes and de-serializes the data of currency.
    """
    class Meta:
        model = Currency
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    """
    Serializes and de-serializes the data of country.
    """
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    """
    Serializes and de-serializes the data of states in countries.
    """
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    """
    Serializes and de-serializes the data of city in states .
    """
    class Meta:
        model = City
        fields = '__all__'


class TimezoneSerializer(serializers.ModelSerializer):
    """
    Serializes and de-serializes the data of timezones.
    """
    class Meta:
        model = Timezone
        fields = '__all__'