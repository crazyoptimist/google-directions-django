from . import views
from django.urls import path

urlpatterns = [
    path(
        "latlng",
        views.get_carbon_emissions_by_latlng,
        name="carbon_emissions_by_latlng",
    )
]
