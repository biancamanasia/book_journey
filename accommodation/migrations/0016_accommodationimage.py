# Generated by Django 5.0.3 on 2024-06-22 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0015_alter_accommodation_number_of_apartments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccommodationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='accommodation_images/')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='accommodation.accommodation')),
            ],
        ),
    ]