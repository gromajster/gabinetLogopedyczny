# Generated by Django 2.2.5 on 2020-01-12 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationToken',
            fields=[
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='visit.Appointment')),
                ('confirmation_link', models.CharField(max_length=255)),
            ],
        ),
    ]
