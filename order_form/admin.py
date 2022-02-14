from django.contrib import admin

from order_form.models import Product
# (('url', 'title'), 'content')
class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('item_number', 'active'),
        'title',
        'description',
        'image',
        ('price_retail', 'price_wholesale', 'quantity', 'quantity_unit'),
        ('product_category', 'chocolate_type'),
        'sugar_free',
        'seasonal',
    )

admin.site.register(Product, ProductAdmin)
