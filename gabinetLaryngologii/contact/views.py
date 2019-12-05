from rest_framework import views
from rest_framework.response import Response

from .serializers import ContactSerializer


class ContactView(views.APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_form = serializer.data

        return Response({"message": "Wiadomość została poprawnie wysłana."}, status=200)
