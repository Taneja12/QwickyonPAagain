# Generated by Django 4.2.4 on 2024-03-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_wishlistt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('c_details', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]