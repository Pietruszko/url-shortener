import pytest
from ..models import ShortenedURL
from django.urls import reverse

@pytest.mark.django_db
def test_redirect_view_redirects_to_original_url(client):
    """Test that the redirect endpoint returns 302 to the original URL."""
    data = {
        "original_url": "https://www.example.com",
        "short_code": "abc123abc1"
    }
    ShortenedURL.objects.create(**data)
    url = reverse('redirect', args=[data['short_code']])
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == data['original_url']

@pytest.mark.django_db
def test_shortenedurl_view_set_create_shortened_url(client):
    """Test that the ShortenedURLViewSet can create a new shortened URL."""
    data = {
        "original_url": "https://www.example.com",
    }
    response = client.post(reverse('shorten'), data)
    assert response.status_code == 201
    assert 'short_code' in response.data
    assert response.data['original_url'] == data['original_url']
    assert ShortenedURL.objects.count() == 1
