from rest_framework import serializers


class PathLatlngSerializer(serializers.Serializer):
    origin = serializers.ListField(child=serializers.FloatField())
    destination = serializers.ListField(child=serializers.FloatField())
