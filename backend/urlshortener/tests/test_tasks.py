import pytest
from ..tasks import track_click
from ..models import ShortenedURL

@pytest.mark.django_db
def test_track_click():
    """Test that the track_click function updates the click count."""
    data = {
        "original_url": "https://www.example.com",
        "short_code": "abc123abc1"
    }
    url = ShortenedURL.objects.create(**data)
    assert url.clicks == 0
    track_click(url)
    url.refresh_from_db()
    assert url.clicks == 1