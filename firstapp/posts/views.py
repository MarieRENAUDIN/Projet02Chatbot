from django.shortcuts import render
from rest_framework import viewsets 
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

# Create your views here.
