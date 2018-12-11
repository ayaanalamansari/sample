from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import Currency, Country, State, City, Timezone
from .serializers import CurrencySerializer, CountrySerializer, StateSerializer,\
                         CitySerializer, TimezoneSerializer
from rest_framework.decorators import detail_route, list_route

class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    *To get all currencies from the database.*
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    *To get all countries from the database.*
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None


class StateViewSet(generics.ListAPIView):
    """
    *To get all the states in a country from the database.*
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    pagination_class = None

    def get_queryset(self):
        """
        Filter all the records based on country Id.
        """
        queryset = super(StateViewSet, self).get_queryset()
        queryset = queryset.filter(country=self.kwargs['pk'])
        return queryset

class CityViewSet(generics.ListAPIView):
    """
    *To get all the cities in a state from the database.*
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = None

    def get_queryset(self):
        """
        Filter the records based on state Id.
        """
        queryset = super(CityViewSet, self).get_queryset()
        queryset = queryset.filter(state=self.kwargs['pk'])
        return queryset


class TimeZoneViewSet(viewsets.ReadOnlyModelViewSet):
    """
    *To get all the timezones from the database.*
    """
    queryset = Timezone.objects.all()
    serializer_class = TimezoneSerializer
    pagination_class = None