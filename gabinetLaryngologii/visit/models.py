from django.db import models

TIME_CHOICES = (
    ('8:00', '8:00'),
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00')
)


class Appointment(models.Model):
    email = models.EmailField()
    surname = models.CharField(max_length=50)
    appointment_date = models.DateField()
    appointment_time = models.CharField(choices=TIME_CHOICES, max_length=5)
    appointment_status = models.CharField(max_length=255, default="open")
