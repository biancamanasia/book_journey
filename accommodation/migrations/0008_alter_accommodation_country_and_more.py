# Generated by Django 5.0.3 on 2024-06-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0007_remove_accommodation_accommodation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='country',
            field=models.CharField(choices=[('Romania', 'Romania'), ('Bulgaria', 'Bulgaria'), ('Cyprus', 'Cyprus'), ('Egypt', 'Egypt'), ('Finland', 'Finland'), ('Greece', 'Greece'), ('Italy', 'Italy'), ('Kenya', 'Kenya'), ('Maldives', 'Maldives'), ('Mauritius', 'Mauritius'), ('Morocco', 'Morocco'), ('Portugal', 'Portugal'), ('Seychelles', 'Seychelles'), ('Spain', 'Spain'), ('Switzerland', 'Switzerland'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('United Arab Emirates', 'United Arab Emirates')], default='Romania', max_length=100),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='star_rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=3),
        ),
    ]
