from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=True)
    phone_number = serializers.IntegerField()
    message = serializers.CharField(max_length=1000)

    def validate(self, attrs):
        print(attrs)
        return attrs
