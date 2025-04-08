from django.shortcuts import get_object_or_404
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer, UserSerializer
from rest_framework import generics, permissions
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from .tasks import track_click
from django.core.cache import cache


class ShortenedURLViewSet(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    permission_classes = [permissions.AllowAny]

class RedirectView(RedirectView):
    def get(self, request, short_code):
        cache_key = f'redirect_{short_code}'
        print(f"Attempting to get cache key: {cache_key}")  # Debug
        
        original_url = cache.get(cache_key)
        if not original_url:
            print("Cache MISS - fetching from DB")
            url = get_object_or_404(ShortenedURL, short_code=short_code)
            original_url = url.original_url
            cache.set(cache_key, original_url, timeout=3600)
            print(f"Cached URL: {cache_key} -> {original_url}")
        else:
            print("Cache HIT")
            
        track_click.delay(short_code)
        print(f"Redirecting to: {original_url}") 
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