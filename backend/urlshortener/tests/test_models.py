import pytest
from ..models import ShortenedURL
from django.db import IntegrityError

@pytest.mark.django_db
def test_shortened_url_creation():
    """Test the creation of a ShortenedURL object."""
    original_url = "https://www.example.com"
    short_code = "abc123abc1"
    shortened_url = ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
    assert shortened_url.original_url == original_url
    assert shortened_url.short_code == short_code
    assert len(shortened_url.short_code) == 10
    assert shortened_url.created_at is not None

@pytest.mark.django_db
def test_shortened_url_unique_short_code():
    """Test that the ShortenedURL model enforces uniqueness of the short_code field."""
    original_url = "https://www.example.com"
    short_code = "abc123abc1"
    ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
    with pytest.raises(IntegrityError):
        ShortenedURL.objects.create(original_url=original_url, short_code=short_code)