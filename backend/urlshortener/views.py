from django.shortcuts import render
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer, UserSerializer
from rest_framework import generics, permissions
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from django.contrib.auth.models import User

# EccBuGEUAn - short code for github.com for tests

class ShortenedURLViewSet(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

class RedirectView(RedirectView):
    def get(self, request, short_code):
        original_url = ShortenedURL.objects.get(short_code=short_code).original_url
        return HttpResponseRedirect(original_url)
    
class ShortenedURLListView(generics.ListAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]