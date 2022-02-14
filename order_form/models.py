from django.conf import settings
from django.db import models
from django.utils import timezone

PRODUCT_CATEGORIES = [
    ('Caramels', (
            ('Grey Sea Salt Caramels','Grey Sea Salt Caramels'),
            ('Huckleberry Caramels','Huckleberry Caramels'),
        )
    ),
    ('Truffles', (
            ('Mocha','Mocha'),
            ('Raspberry','Raspberry'),
        )
    ),
]

QUANTITY_UNIT = [
    ('lbs.', 'lbs.'),
    ('pieces', 'pieces'),
]

class Product(models.Model):
    CHOCOLATE_TYPE = [
        ('Milk', 'Milk'),
        ('Dark', 'Dark'),
        ('White', 'White'),
        ('Other', 'Other'),
        ('N/A', 'N/A'),
    ]
    item_number = models.PositiveSmallIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    quantity_unit = models.CharField(
        max_length=100,
        choices=QUANTITY_UNIT,
        default=''
    )
    image = models.ImageField(upload_to='images', blank=True)
    product_category = models.CharField(
        max_length=100,
        choices=PRODUCT_CATEGORIES
    )
    chocolate_type = models.CharField(
        max_length=100,
        choices=CHOCOLATE_TYPE
    )
    price_retail = models.DecimalField(max_digits=5, decimal_places=2)
    price_wholesale = models.DecimalField(max_digits=5, decimal_places=2)
    #retail/wholesale inherit from product
    #min order for wholesale (e.g. 144/box)
    #if seasonal, when active by month (maybe day?)... auto show based on availability.
    #funtion for quantity, unit, title, chocolate type
    sugar_free = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    seasonal = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.title)