from celery import shared_task
from django.core.mail import send_mail, EmailMessage

from gabinetLaryngologii import settings


@shared_task
def send_confirmation_email(email, subscription_confirmation_url, time, date):
    data = {"confirmation_url": subscription_confirmation_url,
            "subject": "Gabinet Logopedyczny potwierdzenie wizyty",
            "time": time,
            "date": date,
            "email": email,
            "contact_link": "https://gabinetlogopedyczny.mglernest.now.sh/contact"}
    message = f"Dzień dobry! \n" \
              f"Wizyta dnia {data.get('date')}, na godzinę {data.get('time')}, \n" \
              f"jest prawie potwierdzona, wystarczy że klikniesz w poniższy link potwierdzający: \n" \
              f"{data.get('confirmation_url')} \n" \
              f"W przypadku dodatkowych pytań zapraszam do formularza kontaktowego znajdującego się tutaj: \n" \
              f"{data.get('contact_link')}\n" \
              f"Dziękuję i pozdrawiam! \n" \
              f"Joanna Zacniewska"
    email_message = EmailMessage(data["subject"], message, settings.EMAIL_HOST_USER,
                                 [data['email']])

    email_message.send(fail_silently=False)
    return True
