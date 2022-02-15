# Generated by Django 4.0.2 on 2022-02-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0008_alter_location_address_2_alter_location_fax_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='openinghours',
            options={'ordering': ('weekday', 'from_hour'), 'verbose_name_plural': 'Opening Hours'},
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_name',
        ),
        migrations.AlterField(
            model_name='location',
            name='address_1',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Street Address 1'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Street Address 2'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_city',
            field=models.CharField(max_length=100, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_state',
            field=models.CharField(max_length=100, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_zip',
            field=models.CharField(max_length=100, verbose_name='ZIP Code'),
        ),
        migrations.AlterField(
            model_name='location',
            name='fax_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Fax'),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Phone'),
        ),
    ]
