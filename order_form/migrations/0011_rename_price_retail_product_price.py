# Generated by Django 4.0.2 on 2022-02-15 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0010_location_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_retail',
            new_name='price',
        ),
    ]