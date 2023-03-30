from django.http import HttpResponse

import nltk
from nltk.chat.util import Chat, reflections
from django.shortcuts import render
from django. template import loader

from chatbot.models import Echange
import unicodedata



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
      data={}

      return(HttpResponse(template.render(data)))


# programmes
def programmes(request) :
      template= loader.get_template('programmes.html') 
      data={}

      return(HttpResponse(template.render(data)))

# recettes
def recette(request) :
      template= loader.get_template('index.html') 
      data={'page':'recette'}

      return(HttpResponse(template.render(data)))

# conseils
def conseils(request) :
      template= loader.get_template('conseils.html') 
      data={}

      return(HttpResponse(template.render(data)))

# contact
def contact(request) :
      template= loader.get_template('contact.html') 
      data={'page':'contact'}

      return(HttpResponse(template.render(data)))

# contact



def chatbot(request):
   

    if request.method == 'POST':
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
      texte_normalized = unicodedata.normalize('NFKD', question).encode('ASCII', 'ignore').decode('utf-8')
      response = chat.respond(texte_normalized)
      
      # Normalisation Unicode
      messages = [{'sender': 'user', 'text': question}, {'sender': 'bot', 'text': response}]
      return render(request, 'chatbot.html', {'messages': messages})
    else:
        return render(request, 'chatbot.html')
       