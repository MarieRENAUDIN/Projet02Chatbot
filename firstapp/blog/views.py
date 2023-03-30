import nltk
from nltk.chat.util import Chat, reflections
from django.shortcuts import render
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
   

    pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
     [
        r"remplacer viande",
        ["Voici quelques-unes des options les plus courantes : Les légumineuses, les produits à base de soja, les champignons, les substituts de viande à base de plantes.",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Analytics Vidhya. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"Quels sont les différents régimes alimentaires qui existent ?",
        ["Voici plusieurs régimes alimentaires : Régime méditerranéen, Régime végétarien, Régime végan, Régime sans gluten, Régime cétogène, Régime Paléo, Régime flexitarien. Ces régimes ne sont pas exhaustifs et il existe de nombreuses autres options, chacune ayant des avantages et des inconvénients. Il est important de consulter un professionnel de la santé avant de commencer tout régime alimentaire pour s'assurer qu'il répond à vos besoins."]
    ],
    
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

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
       