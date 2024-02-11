# views.py

from rest_framework import serializers
from chat_app.models import Message
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source = 'sender.username')
    main_subject = serializers.CharField(source ='message_subject', read_only = True)
    class Meta:
        model = Message
        fields = ('id', 'sender', 'main_subject', 'subject', 'message_content','timestamp','response')
        read_only_fields = ('id', 'timestamp', 'main_subject')
        depth = 0

class MessageResponseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'message', 'response_content', 'timestamp')
        read_only_fields = ('id', 'timestamp')
        depth = 1  # Adjust the depth based on your model relationships


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_agent', 'is_customer']
