# Generated by Django 5.0.1 on 2024-01-31 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_newsletter_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100, null=True, verbose_name='Estado'),
        ),
    ]
