from django.conf import settings
from django.db import models
from django.utils import timezone

WEEKDAYS = [
  (1, _("Monday")),
  (2, _("Tuesday")),
  (3, _("Wednesday")),
  (4, _("Thursday")),
  (5, _("Friday")),
  (6, _("Saturday")),
  (7, _("Sunday")),
]

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images', blank=True)
    email_address = models.TextField()

class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    fax_number = models.TextField()
    hours = models.ForeignKey(OpeningHours, on_delete=models.CASCADE)
    address_1 = models.TextField()
    address_2 = models.TextField()
    address_city = models.TextField()
    address_state = models.TextField()
    address_zip = models.TextField()

class OpeningHours(models.Model):

    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)
# class Hours(models.Model):
#     location = models.OneToOneField(
#         Location,
#         on_delete=models.CASCADE,
#     )
#     sunday = models.CharField(max_length=100)
#     monday = models.CharField(max_length=100)
#     tuesday = models.CharField(max_length=100)
#     wednesday = models.CharField(max_length=100)
#     thurday = models.CharField(max_length=100)
#     friday = models.CharField(max_length=100)
#     saturday =models.CharField(max_length=100)