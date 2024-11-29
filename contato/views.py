from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

@csrf_exempt
def submit_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        message_text = data.get("message")

        # Salva a mensagem
        Message.objects.create(name=name, email=email, message=message_text)

        return JsonResponse({"status": "success", "message": "Mensagem enviada com sucesso!"})
    return JsonResponse({"status": "error", "message": "Método não permitido."})

def contact_form(request):
    return render(request, 'formulario.html')