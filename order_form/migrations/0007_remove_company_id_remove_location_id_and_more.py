# Generated by Django 4.0.2 on 2022-02-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0006_alter_company_email_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_1',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_zip',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='fax_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
