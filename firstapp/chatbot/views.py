from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from .chatbot import get_bot_response
# Create your views here.
from django.shortcuts import render
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Ajoutez vos paires question / réponse ici
]

def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        oldquestion = request.POST.get('oldechange')
        chat = Chat(pairs, reflections)
        response = chat.respond(question)
        oldechange = oldquestion + question + response
        return render(request, 'chatbot.html', {'messages' : oldechange, 'question': question, 'response': response})
    else:
        return render(request, 'chatbot.html')
    









@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        text = request.POST.get('question')
        oldechange = request.POST.get('oldechange')
        if text:
            message = Message.objects.create(sender='user', text=text)
            response = get_bot_response(text)
            Message.objects.create(sender='bot', text=response)
            oldechange += f"{text}\n{response}\n"
    else:
        oldechange = ''
    messages = Message.objects.all()
    return render(request, 'chatbot.html', {'messages': messages, 'oldechange': oldechange})
