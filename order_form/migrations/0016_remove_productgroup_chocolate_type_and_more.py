# Generated by Django 4.0.2 on 2022-02-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0015_product_product_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productgroup',
            name='chocolate_type',
        ),
        migrations.AddField(
            model_name='productgroup',
            name='dark_chocolate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='milk_chocolate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='not_applicable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='other',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='white_chocolate',
            field=models.BooleanField(default=True),
        ),
    ]