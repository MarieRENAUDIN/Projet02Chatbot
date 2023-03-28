from django.contrib import admin
from django.urls import path
from blog import views


# importe la vue
urlpatterns = [
    path('admin/', admin.site.urls),
    # définie la fonction à appeler

    # accueil
    path("", views.home, name="home"),

    path("programmes", views.programmes, name="programmes"),

    # recettes
    path("recettes", views.recette, name="recettes"),

    # conseiles
    path("conseils", views.conseils, name="conseils"),

    # contact
    path("contact", views.contact, name="contact"),

    # chatbot
    path("chatbot", views.chatbot, name="chatbot")

]
 