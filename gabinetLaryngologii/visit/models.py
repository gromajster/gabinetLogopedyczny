import os

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
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    appointment_date = models.DateField()
    appointment_time = models.CharField(choices=TIME_CHOICES, max_length=5)
    appointment_status = models.CharField(max_length=255, default="open")
    date = {}

    def __str__(self):
        return self.email

    def day(self):
        date = {"day": self.appointment_date.day}
        return date["day"]

    def month(self):
        months = {1: "Styczeń",
                  2: "Luty",
                  3: "Marzec",
                  4: "Kwiecień",
                  5: "Maj",
                  6: "Czerwiec",
                  7: "Lipiec",
                  8: "Sierpień",
                  9: "Wrzesień",
                  10: "Październik",
                  11: "Listopad",
                  12: "Grudzień",
                  }
        month = months[self.appointment_date.month]
        date = {"month": month}
        return date["month"]

    def year(self):
        date = {"year": self.appointment_date.year}
        return date["year"]


class ConfirmationToken(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    confirmation_link = models.CharField(max_length=255)

    def __str__(self):
        return "Token użytkownika o E-mailu: " + self.appointment.email
