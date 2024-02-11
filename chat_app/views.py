
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .models import Message, User

class ChatView(TemplateView):
    template_name = 'chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agents'] = User.objects.filter(is_agent=True)
        return context

class CustomerNewMessage(View):
    def post(self, request, *args, **kwargs):
        message_content = request.POST.get('message_content', '')
        sender_id = request.POST.get('sender_id', '')

        if message_content and sender_id:
            message = Message.objects.create(
                sender_id=sender_id,
                recipient_id=User.objects.get(is_agent=True).id,  # Assign to the first agent for simplicity
                message_content=message_content,
            )
            return JsonResponse({'status': 'success', 'message_id': message.id})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})

class AgentReplyMessage(View):
    def post(self, request, *args, **kwargs):
        message_content = request.POST.get('message_content', '')
        sender_id = request.POST.get('sender_id', '')
        recipient_id = request.POST.get('recipient_id', '')

        if message_content and sender_id and recipient_id:
            message = Message.objects.create(
                sender_id=sender_id,
                recipient_id=recipient_id,
                message_content=message_content,
            )
            return JsonResponse({'status': 'success', 'message_id': message.id})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})


def messages_list(request):
    return render(request, 'messages_list.html')