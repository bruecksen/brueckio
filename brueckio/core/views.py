from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ContactFormSerializer


class ContactFormView(APIView):
    """
    View send contact form as a email

    """

    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            # send email
            try:
                # serializer.data['email']
                message = "First name: %s \nLast name: %s \nEmail: %s \nMessage: %s \n" % (
                    serializer.data['firstname'],
                    serializer.data['lastname'],
                    serializer.data['email'],
                    serializer.data['message']
                )

                send_mail(
                    '[brueck.io] New contact form submission',
                    message,
                    'noreply@brueck.io',
                    ['hi@brueck.io', ],
                )
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response('Sending email failed.', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
