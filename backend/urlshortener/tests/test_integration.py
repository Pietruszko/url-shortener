import pytest
from django.urls import reverse
from ..models import ShortenedURL

@pytest.mark.django_db
def test_full_workflow(client):
    """Test the full workflow of creating a shortened URL."""
    original_url = "https://www.example.com"

    response = client.post(
        reverse('shorten'), data={'original_url': original_url}, content_type='application/json'
    )

    assert response.status_code == 201
    data = response.json()
    short_code = data['short_code']
    
    assert ShortenedURL.objects.count() == 1
    shortened_url = ShortenedURL.objects.first()
    assert shortened_url.original_url == original_url
    assert shortened_url.short_code == short_code

    redirect_response = client.get(
        reverse('redirect', args=[short_code]), follow=False
    )
    assert redirect_response.status_code == 302
    assert redirect_response.url == original_url


@pytest.mark.django_db
def test_error_handlig_flow(client):
    """Test the error handling flow of creating a shortened URL and redirecting."""
    original_url = "www.badurl.com"
    response = client.post(
        reverse('shorten'), data={'original_url': original_url}, content_type='application/json'
    )
    assert response.status_code == 400

    short_code = 'abc123abc1'
    with pytest.raises(ShortenedURL.DoesNotExist):
        response = client.get(reverse('redirect', args=[short_code]), follow=False)
