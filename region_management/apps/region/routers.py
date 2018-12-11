from django.urls import path
from rest_framework.routers import SimpleRouter
from region_management.apps.region import views

router = SimpleRouter()

urlpatterns = [
        path('currencies/', views.CurrencyViewSet.as_view({'get': 'list'}), name='currencies'),
        path('timezones/', views.TimeZoneViewSet.as_view({'get': 'list'}), name='timezones'),
        path('countries/', views.CountryViewSet.as_view({'get': 'list'}), name='countries'),
        path('countries/<int:pk>/states/', views.StateViewSet.as_view(), name='country-state'),
        path('states/<int:pk>/cities/', views.CityViewSet.as_view(), name='state-city'),
]

urlpatterns += router.urls