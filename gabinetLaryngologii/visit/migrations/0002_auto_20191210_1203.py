# Generated by Django 2.2.5 on 2019-12-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.CharField(choices=[(1, '8:00'), (2, '9:00'), (3, '10:00'), (4, '11:00'), (5, '12:00'), (6, '13:00'), (7, '14:00'), (8, '15:00'), (9, '16:00')], max_length=5),
        ),
    ]