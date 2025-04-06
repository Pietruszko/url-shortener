from django.shortcuts import render
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView

# EccBuGEUAn - short code for github.com for tests

class ShortenedURLViewSet(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

class RedirectView(RedirectView):
    def get(self, request, short_code):
        original_url = ShortenedURL.objects.get(short_code=short_code).original_url
        return HttpResponseRedirect(original_url)