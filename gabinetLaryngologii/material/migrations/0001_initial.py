# Generated by Django 2.2.5 on 2019-11-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_name', models.CharField(max_length=100)),
                ('media_url', models.FileField(upload_to='media')),
            ],
        ),
    ]
