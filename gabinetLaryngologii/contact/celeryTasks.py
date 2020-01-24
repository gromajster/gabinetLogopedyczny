from celery import shared_task

from django.core.mail import send_mail
from gabinetLaryngologii import settings


@shared_task
def send_email_task(contact_form):
    message = f"Imię: {contact_form.get('name')} \n" \
              f"Nazwisko: {contact_form.get('surname')} \n" \
              f"E-mail: {contact_form.get('email')} \n" \
              f"Tel.: {contact_form.get('phone_number')} \n" \
              f"Treść wiadomości: \n" \
              f"{contact_form.get('message')}"
    send_mail('Wiadomość Gabinet Logopedyczny', message, settings.EMAIL_HOST_USER, ['mkucko145@gmail.com'])

