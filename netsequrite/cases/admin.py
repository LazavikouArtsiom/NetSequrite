from django.contrib import admin
from .models import Case, Verification, Verification_LocationEquipment, Meeting

admin.site.register(Case)
admin.site.register(Verification)
admin.site.register(Verification_LocationEquipment)
admin.site.register(Meeting)

