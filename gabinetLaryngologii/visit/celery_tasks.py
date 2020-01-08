from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.utils.html import strip_tags

from gabinetLaryngologii import settings


@shared_task
def send_confirmation_email(email, subscription_confirmation_url):
    data = dict()
    # data["confirmation_url"] = subscription_confirmation_url
    # data["subject"] = "Please confirm the subscription"
    data["email"] = email
    # data["project_name"] = "Scientific Dev"
    # data["site_url"] = "https://www.scientificdev.net"
    # data["contact_us_url"] = "https://www.scientificdev.net/contact/"
    # template = get_template("visit_confirmation/confirmation_mail.html")
    # data["html_text"] = template.render(data)
    # data["plain_text"] = strip_tags(data["html_text"])
    #
    # # send_mail(data["subject"], data["plain_text"], settings.EMAIL_HOST_USER, [data['email']])
    # email_message = EmailMessage(data["subject"], data["plain_text"], 'artur@scientificdev.net',
    #                              [data['email']])
    # email_message.send(fail_silently=False)
    message = subscription_confirmation_url
    send_mail('Wiadomość Gabinet Logopedyczny', message, settings.EMAIL_HOST_USER, [data['email']])
    return None
