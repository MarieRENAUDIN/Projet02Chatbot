from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPages(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add= True)

    
    def __str__(self):
        return self.title
class BlogPagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'content')
   