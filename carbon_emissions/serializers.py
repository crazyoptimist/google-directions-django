from rest_framework import serializers


class PathLatlngSerializer(serializers.Serializer):
    origin = serializers.ListField(child=serializers.FloatField())
    destination = serializers.ListField(child=serializers.FloatField())

    def validate(self, data):
        if len(data["origin"]) != 2 or len(data["destination"]) != 2:
            raise serializers.ValidationError("Invalid lat lng format")
        if not validate_latlng(*data["origin"]):
            raise serializers.ValidationError("Invalid origin value")
        if not validate_latlng(*data["destination"]):
            raise serializers.ValidationError("Invalid destination value")
        return data


def validate_latlng(lat, lng):
    """
    Lat is between -90 and 90, Lng is between -180 and 180
    """
    if lat > -90 and lat < 90 and lng > -180 and lng < 180:
        return True
    return False
