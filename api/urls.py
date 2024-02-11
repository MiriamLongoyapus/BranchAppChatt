# urls.py

from django.urls import path
from .views import (
    MessageListView,ReadMessageListView,MessageResponseView,UnReadMessageListView,CustomerNewMessage,MessageReadView
   
)

urlpatterns = [
    path('messages/all/', MessageListView.as_view(), name='all-messages-list'),
    path('read/messages/', ReadMessageListView.as_view(), name='all-messages-response'),
    path('response/messages/<pk>/', MessageResponseView.as_view(), name='messages-response'),
    path('unread/messages/', UnReadMessageListView.as_view(), name='unread-messages'),
    path('new/messages/', CustomerNewMessage.as_view(), name='new-messages'),

]
