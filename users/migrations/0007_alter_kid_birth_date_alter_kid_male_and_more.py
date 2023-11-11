# Generated by Django 4.2.5 on 2023-11-11 16:04

from django.db import migrations, models

import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_address_kid_alter_customuser_options_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='birth_date',
            field=models.CharField(blank=True, null=True, validators=[users.validators.validate_date_format]),
        ),
        migrations.AlterField(
            model_name='kid',
            name='male',
            field=models.CharField(blank=True, choices=[('Boy', 'Male'), ('Girl', 'Female')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.CharField(blank=True, null=True, validators=[users.validators.validate_date_format]),
        ),
    ]