from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from ..models import ChatMessage
import json
from ..Helpers.helper import renderr

def chat_page(request):
    messages = ChatMessage.objects.order_by('-timestamp')[:50]
    return renderr(request, 'chat', {'messages': reversed(messages)})

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '').strip()
            if not message:
                return JsonResponse({'error': 'Empty message'}, status=400)
            msg = ChatMessage.objects.create(message=message)
            return JsonResponse({
                'message': msg.message,
                'timestamp': msg.timestamp.strftime('%H:%M:%S')
            })
        except Exception:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
