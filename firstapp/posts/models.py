from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

# Create your models here.
