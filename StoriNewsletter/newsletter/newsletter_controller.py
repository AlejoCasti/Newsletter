from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response

from newsletter.models import Newsletter, NewsletterHistory, NewsletterEvents, NewsletterStatus
from newsletter.serializer import NewsletterSerializer, NewsletterListSerializer
from services.email import EmailService
from services.jwt import JwtService
from services.storage import StorageService
from services.utils import Utils
from django.db.models import F, Func

User = get_user_model()

DEFAULT_TEMPLATE = 'newsletter_template'


class NewsletterController:
    @staticmethod
    def create_newsletter(user: User, data):
        recipients_emails = data.get('recipients_emails')
        title = data.get('title')
        email_template_name = data.get('email_template_name', DEFAULT_TEMPLATE)
        source_name = data.get('source_name')

        try:
            recipients_emails_list = recipients_emails.split(',')

            newsletter = Newsletter.objects.create(
                title=title,
                recipients_emails=recipients_emails_list,
                source_name=source_name,
                email_template_name=email_template_name,
                created_by=user,
            )

            newsletter_serialized = NewsletterSerializer(newsletter)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(newsletter_serialized.data, status=status.HTTP_200_OK)

    @staticmethod
    def delete_newsletter(user: User, params):
        newsletter_id = params.get('id')

        try:
            newsletter = Newsletter.objects.filter(created_by=user, pk=newsletter_id).first()

            if not newsletter:
                return Response({'error': 'Newsletter not found'}, status=status.HTTP_404_NOT_FOUND)

            newsletter.status = NewsletterStatus.INACTIVE
            newsletter.save()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response('ok', status=status.HTTP_200_OK)

    @staticmethod
    def send_newsletter(data):
        newsletter_id = data.get('id')
        newsletter = Newsletter.objects.filter(pk=newsletter_id).first()

        if not newsletter:
            return Response({'error': 'Newsletter not found'}, status=status.HTTP_404_NOT_FOUND)

        if not newsletter.source_name or not newsletter.recipients_emails:
            return Response({'error': 'Newsletter incomplete'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        newsletter_document = StorageService.download_file(
            file_name=newsletter.source_name
        )

        for email in newsletter.recipients_emails:
            full_unsubscribe_link = Utils.build_link(email=email)
            part_unsubscribe_link = Utils.build_link(email=email, newsletter_id=newsletter_id)

            print(full_unsubscribe_link, part_unsubscribe_link, email)
            # EmailService.send_email_resend()
            EmailService.send_email(
                title=newsletter.title,
                attachment_file_name=newsletter.source_name,
                file=newsletter_document,
                emails=[email],
                email_template_name=newsletter.email_template_name,
                email_params={
                    'full_unsubscribe_link': full_unsubscribe_link,
                    'part_unsubscribe_link': part_unsubscribe_link,
                }
            )

            NewsletterHistory.objects.create(
                newsletter=newsletter,
                event=NewsletterEvents.SENT,
                recipient_email=email,
            )
        # except Exception as e:
        #     print(e)
        #     return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response('Ok', status=status.HTTP_200_OK)

    @staticmethod
    def unsubscribe_newsletter(params):
        try:
            token = params.get('token')

            data = JwtService.decode(token=token)

            user_email = data.get('email', None)
            newsletter_id = data.get('newsletter_id', None)

            if not newsletter_id:
                NewsletterController.full_remove_from_newsletter(email=user_email)
            else:
                NewsletterController.part_remove_from_newsletter(newsletter_id=newsletter_id, email=user_email)

            return Response('ok', status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        # return HttpResponse('<script type="text/javascript">window.close()</script>')

    @staticmethod
    def full_remove_from_newsletter(email: str):
        newsletters = Newsletter.objects.filter(recipients_emails__contains=[email])
        for newsletter in newsletters:
            newsletter.recipients_emails.remove(email)
            newsletter.save()

            NewsletterHistory.objects.create(
                newsletter=newsletter,
                event=NewsletterEvents.UNSUBSCRIBE,
                recipient_email=email,
            )

    @staticmethod
    def part_remove_from_newsletter(newsletter_id: int, email: str):
        newsletter = Newsletter.objects.filter(pk=newsletter_id).first()
        newsletter.recipients_emails.remove(email)
        newsletter.save()

        NewsletterHistory.objects.create(
            newsletter=newsletter,
            event=NewsletterEvents.UNSUBSCRIBE,
            recipient_email=email,
        )

    @staticmethod
    def get_newsletters(user: User):
        newsletters = Newsletter.objects.filter(created_by=user, status=NewsletterStatus.ACTIVE)

        newsletter_serialized = NewsletterListSerializer(newsletters, many=True)
        return Response(newsletter_serialized.data, status=status.HTTP_200_OK)

    @staticmethod
    def get_statistics(user):
        total_emails_sent = NewsletterHistory.objects\
            .filter(event=NewsletterEvents.SENT, newsletter__created_by=user).count()

        newsletters = Newsletter.objects.filter(created_by=user).exclude(recipients_emails__len=0)
        total_active_users = 0
        for new in newsletters:
            total_active_users += len(new.recipients_emails)

        total_unsubscriptions = NewsletterHistory.objects\
            .filter(event=NewsletterEvents.UNSUBSCRIBE, newsletter__created_by=user).count()

        if total_emails_sent == 0:
            unsubscription_rate = 0
        else:
            unsubscription_rate = total_unsubscriptions / total_emails_sent * 100

        response = {
            'total_emails_sent': total_emails_sent,
            'total_active_users': total_active_users,
            'total_unsubscriptions': total_unsubscriptions,
            'unsubscription_rate': round(unsubscription_rate),
        }
        return Response(response, status=status.HTTP_200_OK)
