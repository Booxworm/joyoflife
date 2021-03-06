# Generated by Django 3.0.2 on 2020-01-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200115_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutee',
            name='timeslot',
            field=models.CharField(choices=[(0, '08:00-09:00'), (1, '09:00-10:00'), (2, '10:00-11:00'), (3, '11:00-12:00'), (4, '12:00-13:00'), (5, '13:00-14:00'), (6, '14:00-15:00'), (7, '15:00-16:00'), (8, '16:00-17:00'), (9, '17:00-18:00'), (10, '18:00-19:00'), (11, '19:00-20:00'), (12, '20:00-21:00'), (13, '21:00-22:00')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='timeslot',
            field=models.CharField(choices=[(0, '08:00-09:00'), (1, '09:00-10:00'), (2, '10:00-11:00'), (3, '11:00-12:00'), (4, '12:00-13:00'), (5, '13:00-14:00'), (6, '14:00-15:00'), (7, '15:00-16:00'), (8, '16:00-17:00'), (9, '17:00-18:00'), (10, '18:00-19:00'), (11, '19:00-20:00'), (12, '20:00-21:00'), (13, '21:00-22:00')], default=0, max_length=1),
        ),
    ]
