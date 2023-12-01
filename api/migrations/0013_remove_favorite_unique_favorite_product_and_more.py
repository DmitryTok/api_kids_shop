# Generated by Django 4.2.7 on 2023-12-01 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_gender_alter_kid_birth_date_alter_kid_male_and_more'),
        ('api', '0012_remove_product_color_remove_product_product_size_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='favorite',
            name='unique_favorite_product',
        ),
        migrations.RemoveConstraint(
            model_name='shoppingcart',
            name='unique_shopping_cart',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user',
        ),
        migrations.AddField(
            model_name='favorite',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='users.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shopping_carts', to='users.profile'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('profile', 'product'), name='unique_favorite_product'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('profile', 'product'), name='unique_shopping_cart'),
        ),
    ]
