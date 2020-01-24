from django.views.decorators.csrf import csrf_exempt
from rest_framework import views
from rest_framework.response import Response

from .serializers import ContactSerializer

from .celeryTasks import send_email_task


class ContactView(views.APIView):
    @csrf_exempt
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_form = serializer.data
        send_email_task.delay(contact_form)
        return Response({"message": "Wiadomość została poprawnie wysłana."}, status=200)
