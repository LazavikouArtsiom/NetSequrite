def create_related_to_verification_models(self):
    building_id = self.case.building.id
    location_ids = [location.id for location in BuildingLocation.objects.filter(building_id=building_id)]
    location_equipments_ids = [LocationEquipment.id for LocationEquipment in LocationEquipment.objects.filter(id__in=location_ids)]
    objs = [
        Verification_LocationEquipment(
            location_equipment_id=location_equipments_id,
            verification_id=self.id
        )
        for location_equipments_id
        in location_equipments_ids
    ]
    Verification_LocationEquipment.objects.bulk_create(objs)
    Meeting.objects.create(verification_id=self.id)