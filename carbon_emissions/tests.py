from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse


class CarbonEmissionsByLatLngTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("carbon_emissions_by_latlng")
        self.invalid_format_data = {
            "origin": [20.222],
            "destination": [20.222, 20.222],
        }
        self.invalid_value_data = {
            "origin": [20.222, 222.222],
            "destination": [20.222, 20.222],
        }

    def test_invalid_format_request_data(self):
        """
        it should return 400 when request is wrongly formatted
        """
        response = self.client.post(path=self.url, data=self.invalid_format_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_value_request_data(self):
        """
        it should return 400 when request has invalid values
        """
        response = self.client.post(path=self.url, data=self.invalid_value_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
