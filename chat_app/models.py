

# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from .managers import UserManager

class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    objects = UserManager()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = 'sender_message', blank = True, null = True)
    subject = models.CharField(max_length = 100, default = '')
    message_content = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.now)
    response = models.ForeignKey('self', verbose_name = 'Response', on_delete = models.
    SET_NULL, blank = True, null = True, related_name = 'children')

    def message_subject(self):
         print(self.response)
         if self.response is not None:
              response = get_message_subject(self.response)
              return response.subject
         
    
def get_message_subject(response):
        print(response)
        if response is None:
            return None
        initial_response = response.response
        print(initial_response)
        if initial_response is None:
            return response
        return get_message_subject(initial_response)



