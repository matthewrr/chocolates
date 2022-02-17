from django.conf import settings
from django.db import models
from django.utils import timezone

PRODUCT_CATEGORIES = [
    ('Soft Centers', 'Soft Centers'),
    ('Truffles', 'Truffles'),
    ('Nuts & Chews', 'Nuts & Chews'),
    ('Misc. Candies', 'Misc. Candies'),
    ('Other', 'Other'),
]
QUANTITY_UNIT = [
    ('lbs.', 'lbs.'),
    ('pc', 'piece'),
]

class Product(models.Model):

    # flavor_category = models.CharField(max_length=100, blank=True) #multiple?
    # flavor_subcategory = models.CharField(max_length=100, blank=True) #multiple?
    item_number = models.PositiveSmallIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    product_category = models.CharField(
        max_length=100,
        choices=PRODUCT_CATEGORIES
    )
    milk_chocolate = models.BooleanField(default=True)
    dark_chocolate = models.BooleanField(default=True)
    white_chocolate = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    not_applicable = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    active = models.BooleanField(default=True)
    seasonal = models.BooleanField(default=False)
    #default image?

    def __str__(self):
        return f'{self.title}'
    
class Item(models.Model):
    CHOCOLATE_TYPE = [
        ('M', 'Milk'),
        ('D', 'Dark'),
        ('W', 'White'),
        ('O', 'Other'),
        ('N', 'N/A'),
    ]
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    item_number = models.PositiveSmallIntegerField(primary_key=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    quantity_unit = models.CharField(
        max_length=100,
        choices=QUANTITY_UNIT,
        default=''
    )
    image = models.ImageField(upload_to='images', blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    wholesale = models.BooleanField(default=False)
    #retail/wholesale inherit from product
    #min order for wholesale (e.g. 144/box)
    #if seasonal, when active by month (maybe day?)... auto show based on availability.
    chocolate_type = models.CharField(
        max_length=100,
        choices=CHOCOLATE_TYPE,
        blank=True
    )
    sugar_free = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    seasonal = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.quantity}{self.quantity_unit}' #add chocolate type?
    
    #item num v sku for item v box
    def sku(self):
        return f'{self.product.item_number}-{self.chocolate_type}'
    # def sku(self):
    #     return f'{item_number}'






WEEKDAYS = [
  (1, ("Monday")),
  (2, ("Tuesday")),
  (3, ("Wednesday")),
  (4, ("Thursday")),
  (5, ("Friday")),
  (6, ("Saturday")),
  (7, ("Sunday")),
]

class Company(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    logo = models.ImageField(upload_to='images', blank=True)
    email_address = models.CharField(max_length=100)
    corporate_phone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class OpeningHours(models.Model):

    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')
        verbose_name_plural = 'Opening Hours'
    
    def __str__(self):
        return f'{self.get_weekday_display()}: {self.from_hour} - {self.to_hour}'

class Location(models.Model):
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=True)
    location_phone = models.CharField(verbose_name='Phone', max_length=20, blank=True)
    fax_number = models.CharField(verbose_name='Fax', max_length=20, blank=True)
    hours = models.ManyToManyField(OpeningHours)
    address_1 = models.CharField(verbose_name='Street Address 1', primary_key=True, max_length=100)
    address_2 = models.CharField(verbose_name='Street Address 2', max_length=100, blank=True)
    address_city = models.CharField(verbose_name='City', max_length=100)
    address_state = models.CharField(verbose_name="State", max_length=100)
    address_zip = models.CharField(verbose_name='ZIP Code', max_length=100)

    def open_now(self):
        return 'Not Open'

    def __str__(self):
        return f'{self.address_1}, {self.address_city}, {self.address_state} {self.address_zip}'