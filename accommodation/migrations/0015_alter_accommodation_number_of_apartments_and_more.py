# Generated by Django 5.0.3 on 2024-06-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0014_accommodation_number_of_apartments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='number_of_apartments',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='number_of_rooms',
            field=models.IntegerField(),
        ),
    ]
