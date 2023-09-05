from rest_framework import serializers
from passenger.models import Passengers


class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ['id','first_name','last_name','travel_points']