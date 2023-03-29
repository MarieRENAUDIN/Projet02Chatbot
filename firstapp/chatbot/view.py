# importations
import nltk
from nltk.tokenize import word_tokenize
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# initialisation du chatbot
from nltk.chat.util import Chat, reflections
pairs = [
    # Paires de questions / réponses
    [
        r"mon nom est (.*)",
        ["Bonjour %1, comment puis-je vous aider ?"]
    ],
    [
        r"comment vas-tu ?",
        ["Je vais bien, merci! Et vous ?"]
    ],
    [
        r"au revoir",
        ["Au revoir, à bientôt !"]
    ]
]
chatbot = Chat(pairs, reflections)

# Vue pour le chatbot
@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        tokens = word_tokenize(message)
        response = chatbot.respond(message)
        data = {'message': response}
        return JsonResponse(data)
    else:
        return render(request, 'chatbot.html')