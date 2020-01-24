from datetime import date

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import EmailMessage

from gabinetLaryngologii import settings
from gabinetLaryngologii.visit.models import Appointment


@shared_task
def send_confirmation_email(email, subscription_confirmation_url, time, date_app):
    message = f"Dzień dobry! \n" \
              f"Wizyta dnia {date_app}, na godzinę {time}, \n" \
              f"jest prawie potwierdzona, wystarczy że klikniesz w poniższy link potwierdzający: \n" \
              f"{subscription_confirmation_url} \n" \
              f"W przypadku dodatkowych pytań zapraszam do formularza kontaktowego znajdującego się tutaj: \n" \
              f"{settings.CONTACT_URL} \n" \
              f"Dziękuję i pozdrawiam! \n" \
              f"Joanna Zacniewska"
    email_message = EmailMessage("Gabinet Logopedyczny potwierdzenie wizyty", message, settings.EMAIL_HOST_USER,
                                 [email])

    email_message.send(fail_silently=False)


@periodic_task(run_every=(crontab(minute=0, hour=18)),
               name='remove_old_appointments_from_db',
               ignore_result=True
               )
#TODO CHECKED IF IT WORKS, CHANGE THE CRON TO 1 MINUTES e.g.
def remove_old_appointments_from_db():
    current_date = date.today()
    Appointment.objects.filter(appointment_date=current_date).delete()
