# Generated by Django 4.2.7 on 2024-07-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_address_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
