from rest_framework import serializers

class ContactFormSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()