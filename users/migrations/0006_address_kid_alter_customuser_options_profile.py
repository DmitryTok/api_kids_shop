# Generated by Django 4.2.5 on 2023-10-19 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_delivery_address', models.CharField()),
                ('second_delivery_address', models.CharField(blank=True, null=True)),
                ('city', models.CharField()),
                ('street', models.CharField()),
                ('building', models.CharField()),
                ('apartment', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.CharField(choices=[('Male', 'Boy'), ('Female', 'Girl')])),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=125, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=125, null=True)),
                ('last_name', models.CharField(blank=True, max_length=125, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('first_phone', models.IntegerField(blank=True, null=True)),
                ('second_phone', models.IntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_address', to='users.address')),
                ('kids', models.ManyToManyField(blank=True, related_name='profile_kids', to='users.kid')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
