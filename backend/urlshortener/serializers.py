from rest_framework import serializers
from .models import ShortenedURL
import random
import string
from django.contrib.auth.models import User

def generate_short_code(lenght=10):
        alphabet = string.ascii_letters + string.digits
        return ''.join(random.choice(alphabet) for _ in range(lenght))

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['original_url', 'short_code', 'created_at', 'user']
        extra_kwargs = {
            'short_code': {'read_only': True},
            'created_at': {'read_only': True},
            'user': {'read_only': True},
        }

    def create(self, data):
        request = self.context.get('request', None)
        user = request.user if request and request.user.is_authenticated else None
        original_url = data['original_url']
        short_code = generate_short_code()
        while ShortenedURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()
        shortened_url = ShortenedURL.objects.create(
            original_url=original_url, 
            short_code=short_code, 
            user=user
            )
        shortened_url.save()
        return shortened_url
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user