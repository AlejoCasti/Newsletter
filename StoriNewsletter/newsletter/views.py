from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from newsletter.models import Newsletter, NewsletterHistory, NewsletterEvents
from newsletter.newsletter_controller import NewsletterController
from newsletter.serializer import NewsletterSerializer
from services.email import EmailService
from services.storage import StorageService


class CreateNewsletter(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        return NewsletterController.create_newsletter(user=request.user, data=request.data)


class DeleteNewsletter(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def delete(request, *args, **kwargs):
        return NewsletterController.delete_newsletter(user=request.user, params=kwargs)


class SendNewsletter(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        return NewsletterController.send_newsletter(data=request.data)


class UnsubscribeNewsletter(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        return NewsletterController.unsubscribe_newsletter(params=kwargs)


class GetNewsletters(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, *args, **kwargs):
        return NewsletterController.get_newsletters(user=request.user)


class Statistics(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, *args, **kwargs):
        return NewsletterController.get_statistics(user=request.user)
