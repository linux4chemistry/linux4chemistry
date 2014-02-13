from django.contrib import admin
from l4c.models import Software, LicenseModel, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)



class LicenseModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(LicenseModel, LicenseModelAdmin)



class SoftwareAdmin(admin.ModelAdmin):
    pass


admin.site.register(Software, SoftwareAdmin)
