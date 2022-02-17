# Generated by Django 4.0.2 on 2022-02-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0012_remove_product_price_wholesale_product_wholesale'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('item_number', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('product_category', models.CharField(choices=[('Soft Centers', 'Soft Centers'), ('Truffles', 'Truffles'), ('Nuts & Chews', 'Nuts & Chews'), ('Misc. Candies', 'Misc. Candies'), ('Other', 'Other')], max_length=100)),
                ('chocolate_type', models.CharField(choices=[('M', 'Milk'), ('D', 'Dark'), ('W', 'White'), ('O', 'Other'), ('N', 'N/A')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='chocolate_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
