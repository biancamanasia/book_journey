# Generated by Django 5.0.3 on 2024-06-22 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0016_accommodationimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='image',
        ),
    ]
