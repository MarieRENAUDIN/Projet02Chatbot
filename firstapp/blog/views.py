from django.http import HttpResponse

import nltk
from nltk.chat.util import Chat, reflections
from django.shortcuts import render
from django. template import loader
from django.views.decorators.csrf import csrf_exempt

from chatbot.models import Echange
import unicodedata
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect

import json
import ast


# Create your views here.
def home(request):
# Exemple de page HTML, non valide pour que l'exemple soit concis
    text ="<h1>Bienvenue sur mon blog !</h1>"
    text = text+ "<p>premier texte de présentation !</p>"

    template= loader.get_template('index.html')
    #strAge = request.GET['age']
    data={'prenom': 'tekfa', 
          'montres':['tissot', 'mondaine','seiko'],
          'page':'home'
    }
    
    return(HttpResponse(template.render(data)))
# accueil
def index(request) :
      template= loader.get_template('index.html') 
      data={'page':'index'}

      return(HttpResponse(template.render(data)))


# programmes
def programmes(request) :
      template= loader.get_template('programmes.html') 
      data={'page':'programmes'}

      return(HttpResponse(template.render(data)))

# recettes
def recette(request) :
      template= loader.get_template('recettes.html') 
      data={'page':'recettes'}

      return(HttpResponse(template.render(data)))

# conseils
def conseils(request) :
      template= loader.get_template('conseils.html') 
      data={'page':'conseils'}

      return(HttpResponse(template.render(data)))

# contact
def contact(request) :
      template= loader.get_template('contact.html') 
      data={'page':'contact'}
      
      return(HttpResponse(template.render(data)))

# chatbot
def chatbot(request) :
      template= loader.get_template('chatbot.html') 
      data={'page':'chatbot'}
      
      return(HttpResponse(template.render(data)))

@csrf_exempt
def chatbot(request):
      template= loader.get_template('chatbot.html') 
      data={'page':'chatbot'}
      data['history']= []
      data['history'].append({'type': 'bot', 'content': "Bonjour, que puis-je faire pour vous ?"})

      if request.method == 'POST':

            # on récupère le champs caché sur le formulaire qui contient l'historique si on a déjà discuté avec le chatbot
            texthistory = request.POST['history']
            # si on a un historique dans le champs, il faut le récupérer au format json
            ##### penser à faire un "import json" en début de programme
            if (texthistory):
                  json_dat = json.dumps(ast.literal_eval(texthistory))
                  data['history'] = json.loads(json_dat)
            pairs = []
            for question_reponse in Echange.objects.all():
                  question = question_reponse.question
                  reponse = question_reponse.reponse
                  # Création de la paire de question-réponse correspondante
                  pair = [r"{}".format(question), reponse.split("|")]
                  # Ajout de la paire à la liste des paires
                  pairs.append(pair)
            
            chat = Chat(pairs, reflections)
            question = request.POST.get('question')
            # Normalisation Unicode
            texte_normalized = unicodedata.normalize('NFKD', question).encode('ASCII', 'ignore').decode('utf-8')
      
            reponse = chat.respond(texte_normalized)
            # on conserve les échange dans l'historique
            msgUser = {"type" : "user", "content": question}
            data['history'].append(msgUser)

            msgBot = {"type" : "bot", "content": reponse}
            data['history'].append(msgBot)

      return(HttpResponse(template.render(data)))
      # 

# def chatbot(request):
#     # Récupération des messages précédents depuis la variable de session
#     messages = request.session.get('messages', [])

#     if request.method == 'POST':
#         pairs = []
#         for question_reponse in Echange.objects.all():
#             question = question_reponse.question
#             reponse = question_reponse.reponse
#             # Création de la paire de question-réponse correspondante
#             pair = [r"{}".format(question), reponse.split("|")]
#             # Ajout de la paire à la liste des paires
#             pairs.append(pair)

#         chat = Chat(pairs, reflections)
#         question = request.POST.get('question')
#         texte_normalized = unicodedata.normalize('NFKD', question).encode('ASCII', 'ignore').decode('utf-8')
#         response = chat.respond(texte_normalized)

#         # Normalisation Unicode
#         messages.append({'sender': 'user', 'text': question})
#         for reponse in response.split("|"):
#             messages.append({'sender': 'bot', 'text': reponse})

#         # Stockage des messages dans la variable de session
#         request.session['messages'] = messages
#         request.session.modified = True

#     else:
#         pairs = []
#         for question_reponse in Echange.objects.all():
#             question = question_reponse.question
#             reponse = question_reponse.reponse
#             # Création de la paire de question-réponse correspondante
#             pair = [r"{}".format(question), reponse.split("|")]
#             # Ajout de la paire à la liste des paires
#             pairs.append(pair)

#         chat = Chat(pairs, reflections)
#         messages.append({'sender': 'bot', 'text': "Bonjour, que puis-je faire pour vous ?"})

#     return render(request, 'chatbot.html', {'messages': messages})
