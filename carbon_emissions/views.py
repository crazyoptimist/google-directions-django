from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(http_method_names=["POST"])
def get_carbon_emissions_by_latlng(request: Request):
    return Response(data=request.data, status=status.HTTP_200_OK)
