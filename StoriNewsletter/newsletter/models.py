from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class NewsletterEvents(models.TextChoices):
    SENT = 'sent'
    SCHEDULED = 'scheduled'
    UNSUBSCRIBE = 'unsubscribe'


class NewsletterStatus(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class Newsletter(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=250, blank=True, null=False)
    recipients_emails = ArrayField(
        models.EmailField(),
        blank=True,
        null=True,
        verbose_name='Correos destinatarios',
    )
    source_name = models.CharField(verbose_name='Nombre clave', max_length=250, blank=True, null=True)
    email_template_name = models.CharField(verbose_name='Plantilla de correo', max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Fecha creacion', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualizacion', auto_now=True)
    status = models.CharField(
        verbose_name='Estado',
        choices=NewsletterStatus.choices,
        max_length=100,
        blank=True,
        null=True,
        default=NewsletterStatus.ACTIVE
    )

    class Meta:
        db_table = 'newsletter'


class NewsletterHistory(models.Model):
    event = models.CharField(
        verbose_name='Tipo de evento',
        max_length=250,
        choices=NewsletterEvents.choices,
        blank=True,
        null=False
    )
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, null=True)
    description = models.CharField(verbose_name='Descripcion', max_length=250, blank=True, null=True)
    recipient_email = models.EmailField(verbose_name='Correo destinatario')
    created_at = models.DateTimeField(verbose_name='Fecha creacion', auto_now_add=True)

    class Meta:
        db_table = 'newsletter_history'
