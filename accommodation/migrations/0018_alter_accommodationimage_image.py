# Generated by Django 5.0.3 on 2024-06-22 15:06

import accommodation.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0017_remove_accommodation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationimage',
            name='image',
            field=models.ImageField(upload_to=accommodation.models.accommodation_image_upload_path),
        ),
    ]
