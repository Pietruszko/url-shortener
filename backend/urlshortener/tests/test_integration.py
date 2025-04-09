import pytest
from django.urls import reverse
from ..models import ShortenedURL
from rest_framework.test import APIClient

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
    ShortenedURL.objects.all().delete()
    response = client.get(reverse('redirect', args=[short_code]), follow=True)
    assert response.status_code == 404

@pytest.mark.django_db
def test_full_workflow_authenticated_user(client):
    """Test the full workflow of registering an account, logging in, creating shortened url for user and accessing user's urls list."""
    client = APIClient()

    user_data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response_register = client.post(reverse('register'), data=user_data)
    assert response_register.status_code == 201

    response_login = client.post(reverse('login'), data=user_data)
    assert response_login.status_code == 200
    token = response_login.data['access']
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    original_url = "https://www.example.com"
    response_create = client.post(reverse('shorten'), data={'original_url': original_url})
    assert response_create.status_code == 201
    shortened_url = ShortenedURL.objects.first()
    assert shortened_url.original_url == original_url
    assert shortened_url.user.username == user_data['username']

    response_list = client.get(reverse('list'))
    assert response_list.status_code == 200
    assert len(response_list.data) == 1
    assert shortened_url.short_code == response_list.data[0]['short_code']
    
    

