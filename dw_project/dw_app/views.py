from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PersonVehicle
from .serializers import PersonVehicleSerializer

@api_view(['POST'])
def person_vehicle(request):
    """
    View called by a POST request to add or update information
    """

    # Deserialize information provided in the request
    ser = PersonVehicleSerializer(data=request.data)

    # Validate provided information
    ser.is_valid(raise_exception=True)

    # Save information to the warehouse
    ser.save()

    return Response({'All good, everything has been saved.'})
