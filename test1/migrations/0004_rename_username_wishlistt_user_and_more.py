# Generated by Django 4.2.4 on 2024-03-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistt',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='wishlistt',
            name='wl_details',
        ),
        migrations.AddField(
            model_name='wishlistt',
            name='products',
            field=models.ManyToManyField(related_name='wishlist', to='test1.product'),
        ),
    ]
