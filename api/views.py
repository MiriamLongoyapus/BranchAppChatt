from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from chat_app.models import Message, User
from .serializers import MessageSerializer

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ReadMessageListView(generics.ListAPIView):
    queryset = Message.objects.filter(is_read=True)
    serializer_class = MessageSerializer

class MessageReadView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UnReadMessageListView(generics.ListAPIView):
    queryset = Message.objects.filter(is_read=False)
    serializer_class = MessageSerializer

class MessageResponseView(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True
        instance.save()
        return super().retrieve(request, *args, **kwargs)

class CustomerNewMessage(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
           serializer.save(sender = self.request.user)
        else:
           serializer.save()
   



class CustomerResponseMessageView(MessageResponseView):
    pass


