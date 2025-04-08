import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_register_user(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = client.post(reverse('register'), data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_login_user(client):
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    User.objects.create_user(**data)
    response = client.post(reverse('login'), data)
    assert response.status_code == 200
    assert 'refresh' in response.data and 'access' in response.data

@pytest.mark.django_db
def test_shortened_url_list_authenticated(client):
    user = User.objects.create_user(username='testuser', password='testpass')
    token = str(AccessToken.for_user(user))
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    response = client.get(reverse('list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_shortened_url_list_unauthenticated(client):
    response = client.get(reverse('list'))
    assert response.status_code == 401

    