from django.db import models
from django.contrib import admin

# Create your models here.
class Echange(models.Model):
    question = models.TextField()
    reponse = models.TextField()

    
    def __str__(self):
      return self.question
class EchangeAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse')
    list_filter = ('question',)
   
# Create your models here.
