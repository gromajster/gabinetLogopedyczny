# Generated by Django 2.2.5 on 2019-11-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media_url',
            field=models.FileField(upload_to='media/'),
        ),
    ]
