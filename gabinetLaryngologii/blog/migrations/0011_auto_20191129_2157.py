# Generated by Django 2.2.5 on 2019-11-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191129_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.TimeField(),
        ),
    ]
