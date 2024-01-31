from rest_framework import serializers
from newsletter.models import Newsletter


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id', 'title')


class NewsletterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id', 'title', 'recipients_emails', 'source_name')
