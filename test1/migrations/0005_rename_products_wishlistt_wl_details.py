# Generated by Django 4.2.4 on 2024-03-09 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0004_rename_username_wishlistt_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistt',
            old_name='products',
            new_name='wl_details',
        ),
    ]
