from django.http import HttpResponse
from django.shortcuts import render
from django. template import loader

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
          'montres':['tissot', 'mondaine','seiko']    
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
      template= loader.get_template('recettes.html') 
      data={}

      return(HttpResponse(template.render(data)))

# conseils
def conseils(request) :
      template= loader.get_template('conseils.html') 
      data={}

      return(HttpResponse(template.render(data)))

# contact
def contact(request) :
      template= loader.get_template('contact.html') 
      data={}

      return(HttpResponse(template.render(data)))
