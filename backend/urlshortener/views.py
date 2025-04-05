from django.shortcuts import render
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer
from rest_framework import generics

class ShortenedURLViewSet(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
            
