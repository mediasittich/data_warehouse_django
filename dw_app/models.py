from django.db import models
from simple_history.models import HistoricalRecords

class Person(models.Model):
    """ Person class is a unique physical person identified by first name, last name & email"""

    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Vehicle(models.Model):
    """ Vehicle class stores unique registration plate number"""
    registration_plate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return registration_plate


class PersonVehicle(models.Model):
    """ PersonVehicle registers a relationship between a vehicle and a person """
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        unique_together = (('vehicle'),)

    def __str__(self):
        return '{} {}'.format(self.person, self.vehicle)
    