from rest_framework import serializers
from .models import ShortenedURL
import random
import string

def generate_short_code(lenght=10):
        alphabet = string.ascii_letters + string.digits
        return ''.join(random.choice(alphabet) for _ in range(lenght))

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['original_url', 'short_code', 'created_at']
        extra_kwargs = {
            'short_code': {'read_only': True},
            'created_at': {'read_only': True},
        }

    def create(self, data):
        original_url = data['original_url']
        short_code = generate_short_code()
        while ShortenedURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()
        shortened_url = ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
        return shortened_url