from django.contrib import admin
from order_form.models import *

class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('item_number', 'active'),
        'title',
        'description',
        'image',
        ('price', 'quantity', 'quantity_unit', 'wholesale'),
        ('product_category', 'chocolate_type'),
        'sugar_free',
        'seasonal',
    )

class CompanyAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'logo',
        'email_address',
    )
    class Meta: 
        verbose_name = "Company"
        verbose_name_plural = "Companies"

class OpeningHoursAdmin(admin.ModelAdmin):
    fields = (
        'weekday',
        'from_hour',
        'to_hour',
    )

class LocationAdmin(admin.ModelAdmin):
    fields = (
        'company',
        ('phone_number', 'fax_number'),
        'hours',
        'address_1',
        'address_2',
        'address_city',
        'address_state',
        'address_zip',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(OpeningHours, OpeningHoursAdmin)
admin.site.register(Location, LocationAdmin)