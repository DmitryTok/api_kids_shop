# Generated by Django 4.2.4 on 2023-08-14 12:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_product_is_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.discount'),
        ),
    ]