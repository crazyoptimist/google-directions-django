import os
from urllib.parse import urlencode
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from .serializers import PathLatlngSerializer

GOOGLE_DIRECTIONS_API_BASE_URL = "https://maps.googleapis.com/maps/api/directions/json"
carbon_consumption = {
    "driving": 0.192,
    "train": 0.041,
    "walking": 0,
}


@api_view(http_method_names=["POST"])
def get_carbon_emissions_by_latlng(request: Request):
    serializer = PathLatlngSerializer(instance=request.data)
    origin = serializer.data["origin"]
    destination = serializer.data["destination"]

    distance_driving, duration_driving = get_distance_duration(
        get_endpoint_driving(origin, destination)
    )
    distance_train, duration_train = get_distance_duration(
        get_endpoint_train(origin, destination)
    )
    distance_walking, duration_walking = get_distance_duration(
        get_endpoint_walking(origin, destination)
    )
    return Response(
        data={
            "driving_distance": distance_driving,
            "driving_time": duration_driving,
            "driving_carbon": distance_driving * carbon_consumption["driving"],
            "walking_distance": distance_walking,
            "walking_time": duration_walking,
            "walking_carbon": 0.0,
            "train_distance": distance_train,
            "train_time": duration_train,
            "train_carbon": distance_driving * carbon_consumption["train"],
        },
        status=status.HTTP_200_OK,
    )


def get_distance_duration(google_directions_endpoint):
    result = requests.get(google_directions_endpoint)
    google_response = result.json()
    legs = google_response["routes"][0]["legs"]
    distance = 0
    duration = 0
    for leg in legs:
        distance += leg["distance"]["value"]
        duration += leg["duration"]["value"]
    return distance, duration


def get_endpoint_driving(origin, destination):
    params = {
        "origin": f"{origin[0]},{origin[1]}",
        "destination": f"{destination[0]},{destination[1]}",
        "key": os.getenv("GOOGLE_API_KEY"),
    }
    return f"{GOOGLE_DIRECTIONS_API_BASE_URL}?{urlencode(params)}"


def get_endpoint_train(origin, destination):
    params = {
        "origin": f"{origin[0]},{origin[1]}",
        "destination": f"{destination[0]},{destination[1]}",
        "key": os.getenv("GOOGLE_API_KEY"),
        "mode": "transit",
        "transit_mode": "train",
    }
    return f"{GOOGLE_DIRECTIONS_API_BASE_URL}?{urlencode(params)}"


def get_endpoint_walking(origin, destination):
    params = {
        "origin": f"{origin[0]},{origin[1]}",
        "destination": f"{destination[0]},{destination[1]}",
        "key": os.getenv("GOOGLE_API_KEY"),
        "mode": "walking",
    }
    return f"{GOOGLE_DIRECTIONS_API_BASE_URL}?{urlencode(params)}"
