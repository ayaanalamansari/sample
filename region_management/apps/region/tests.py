from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Currency, Country, State, City, Timezone


class CurrencyTests(APITestCase):
    """
    Test case to check the list of currencies.
    """
    def test_currency_view_list(self):
        url = reverse('currencies')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class CountryTests(APITestCase):
    """
    Test case to check the lits of countries
    """
    def test_country_view_list(self):
        url = reverse('countries')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class StateTests(APITestCase):
    """
    Test case to check the lits of states
    """
    def test_state_view_list(self):
        url = reverse('state', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

class CityTests(APITestCase):
    """
    Test case to check the lits of cities
    """
    def test_city_view_list(self):
        url = reverse('city', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class TimeZoneTests(APITestCase):
    """
    Test case to check the lits of timezones
    """
    def test_time_zone_view_list(self):
        url = reverse('timezones')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
