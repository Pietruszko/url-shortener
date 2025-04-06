import pytest
from ..models import ShortenedURL

@pytest.mark.django_db
def test_shortened_url_creation():
    original_url = "https://www.example.com"
    short_code = "abc123abc1"
    shortened_url = ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
    assert shortened_url.original_url == original_url
    assert shortened_url.short_code == short_code
    assert len(shortened_url.short_code) == 10
    assert shortened_url.created_at is not None