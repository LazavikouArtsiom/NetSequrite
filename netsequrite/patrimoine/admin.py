from django.contrib import admin
from .models import Equipment, Location, Building, LocationEquipment, BuildingLocation

admin.site.register(Equipment)
admin.site.register(Location)
admin.site.register(Building)
admin.site.register(LocationEquipment)
admin.site.register(BuildingLocation)


