# Generated by Django 2.2.5 on 2020-01-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0003_auto_20200114_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(default='Open', max_length=255),
        ),
    ]
