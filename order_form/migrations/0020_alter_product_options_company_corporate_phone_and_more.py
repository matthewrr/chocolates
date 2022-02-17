# Generated by Django 4.0.2 on 2022-02-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0019_rename_productgroup_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AddField(
            model_name='company',
            name='corporate_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='location',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]