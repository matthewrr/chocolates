# Generated by Django 4.0.2 on 2022-02-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_unit',
            field=models.CharField(choices=[('lbs.', 'lbs.'), ('pieces', 'pieces')], default='', max_length=100),
        ),
    ]