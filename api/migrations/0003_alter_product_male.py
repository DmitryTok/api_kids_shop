# Generated by Django 4.2.7 on 2024-04-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='male',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0),
        ),
    ]
