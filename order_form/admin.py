from django.contrib import admin
from order_form.models import *

class ProductAdmin(admin.ModelAdmin):
    fields = (
        'item_number',
        'title',
        'product_category',
        ('milk_chocolate', 'dark_chocolate', 'white_chocolate', 'other', 'not_applicable'),
        'description',
        'active',
        'seasonal',
    )
    list_display = ('title', 'product_category', 'item_number')

class ItemAdmin(admin.ModelAdmin):
    fields = (
        'product',
        ('item_number', 'active'),
        'description',
        'image',
        ('price', 'quantity', 'quantity_unit', 'wholesale'),
        'chocolate_type',
        'sugar_free',
        'seasonal',
    )
    list_display = ('product', 'chocolate_type', 'quantity', 'price', 'item_number', 'sku')

class CompanyAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'logo',
        'corporate_phone',
        'email_address',
    )

class OpeningHoursAdmin(admin.ModelAdmin):
    fields = (
        'weekday',
        'from_hour',
        'to_hour',
    )

class LocationAdmin(admin.ModelAdmin):
    fields = (
        'company',
        'nickname',
        ('location_phone', 'fax_number'),
        'hours',
        'address_1',
        'address_2',
        'address_city',
        'address_state',
        'address_zip',
    )
    list_display = ('nickname','__str__', 'location_phone')

admin.site.register(Item, ItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(OpeningHours, OpeningHoursAdmin)
admin.site.register(Location, LocationAdmin)