# Generated by Django 5.0.2 on 2024-02-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0003_remove_message_responding_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]
