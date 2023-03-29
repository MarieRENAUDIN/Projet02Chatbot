from django.http import HttpResponse
from django.shortcuts import render
from django. template import loader
from django.shortcuts import render
import nltk
from nltk.chat.util import Chat, reflections


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

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
    pairs = [
    ['Bonjour', 'Bonjour ! Comment puis-je vous aider ?'],
    ['Comment ça va ?', 'Je suis un programme, je n\'ai pas d\'émotions, mais merci de demander ! Et vous ?'],
    ['Quel est ton nom ?', 'Je m\'appelle Chatbot. Et vous ?'],
    ['Quel est le sens de la vie ?', 'C\'est une question complexe, je ne suis pas sûr d\'avoir la réponse. Mais certains pensent que c\'est 42.'],
    ['Comment vas-tu ?', 'Je vais bien, merci ! Et vous ?'],
    ['Quelle est la météo aujourd\'hui ?', 'Je suis désolé, je ne peux pas vous fournir la météo actuelle.'],
    ['Comment puis-je vous aider ?', 'Je peux répondre à vos questions ou vous donner des informations sur différents sujets.'],
    ['Qui est le président de la France ?', 'Le président de la France est actuellement Emmanuel Macron.'],
    ['Quel est le plus grand pays du monde ?', 'Le plus grand pays du monde est la Russie.'],
]
    if request.method == 'POST':
        question = request.POST.get('question')
        chat = Chat(pairs, reflections)
        response = chat.respond(question) 
        return render(request, 'chatbot.html', {'question': question, 'response': response})
    else:
            return render(request, 'chatbot.html')
 

      