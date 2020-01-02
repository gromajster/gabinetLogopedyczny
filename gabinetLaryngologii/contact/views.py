from rest_framework import views
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.views import exception_handler

from gabinetLaryngologii import settings
from .serializers import ContactSerializer

from .celery_tasks import send_email_task


class ContactView(views.APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_form = serializer.data
        send_email_task.delay(contact_form)
        return Response({"message": "Wiadomość została poprawnie wysłana."}, status=200)
