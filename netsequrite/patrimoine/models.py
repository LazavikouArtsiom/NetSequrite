from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Location(models.Model):
    name = models.CharField(max_length=255)
    equipments = models.ManyToManyField(Equipment, blank=True, through='LocationEquipment')

    def __str__(self):
        return f'{self.name}'


class Building(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    locations = models.ManyToManyField(Location, blank=True, through='BuildingLocation')

    def __str__(self):
        return f'{self.name} | {self.address}'


class BuildingLocation(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.building} | {self.location}'


class LocationEquipment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.location} | {self.equipment}'
