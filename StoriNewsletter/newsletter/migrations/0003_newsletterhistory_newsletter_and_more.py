# Generated by Django 5.0.1 on 2024-01-28 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_remove_newsletter_source_url_newsletter_source_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterhistory',
            name='newsletter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newsletter.newsletter'),
        ),
        migrations.AlterField(
            model_name='newsletterhistory',
            name='event',
            field=models.CharField(blank=True, choices=[('sent', 'Sent'), ('scheduled', 'Scheduled'), ('unsubscribe', 'Unsubscribe')], max_length=250, verbose_name='Tipo de evento'),
        ),
    ]