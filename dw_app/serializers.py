from rest_framework import serializers

from .models import Person, Vehicle, PersonVehicle

class VehicleSerializer(serializers.Serializer):
    """
    All vehicles that belong to a person will be nested as a list into the JSON representing that person 
    """

    registration_plate = serializers.CharField(max_length=100)

class PersonVehicleSerializer(serializers.Serializer):
    """ Deserializes JSON to be then imported into the data warehouse """
    
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    vehicles = VehicleSerializer(many=True)

    def save(self):
        """
        Custom save function: enables control over how to onsert/update
        the data provided by the source into the data warehouse
        """

        # First update or create a Person
        person_obj, created = Person.objects.update_or_create(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            defaults={'email': self.validated_data['email']},
        )

        # Then create each Vehicle and link it to the Person created before
        for vehicle in self.validated_data['vehicles']:
            vehicle_obj, created = Vehicle.objects.get_or_create(
                registration_plate=vehicle['registration_plate']
            )
            personvehicle_obj, created = PersonVehicle.objects.update_or_create(
                vehicle=vehicle_obj,
                defaults={'person': person_obj},
            )
