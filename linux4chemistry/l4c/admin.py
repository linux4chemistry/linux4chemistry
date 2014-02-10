from django.contrib import admin
from l4c.models import Software

class SoftwareAdmin(admin.ModelAdmin):
    pass

admin.site.register(Software, SoftwareAdmin)
