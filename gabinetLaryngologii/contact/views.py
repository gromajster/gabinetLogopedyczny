from rest_framework import views
from rest_framework.response import Response
from django.core.mail import send_mail

from gabinetLaryngologii import settings
from .serializers import ContactSerializer


class ContactView(views.APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_form = serializer.data
        message = f"Imię: {contact_form.get('name')} \n" \
                  f"Nazwisko: {contact_form.get('surname')} \n" \
                  f"E-mail: {contact_form.get('email')} \n" \
                  f"Tel.: {contact_form.get('phone_number')} \n" \
                  f"Treść wiadomości: \n" \
                  f"{contact_form.get('message')}"
        send_mail('Wiadomość Gabinet Laryngologiczny', message, settings.EMAIL_HOST_USER, ['mkucko145@gmail.com'])
        return Response({"message": "Wiadomość została poprawnie wysłana."}, status=200)
