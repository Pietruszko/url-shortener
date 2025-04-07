import pytest
from ..serializers import ShortenedURLSerializer
from ..models import ShortenedURL

@pytest.mark.django_db
def test_shortenedurl_serializer_create_valid_data():
    """Test that the ShortenedURLSerializer can create a new shortened URL with valid data."""
    data = {
        "original_url": "https://www.example.com",
    }
    serializer = ShortenedURLSerializer(data=data)
    assert serializer.is_valid()
    serializer.save()
    assert serializer.data['original_url'] == data['original_url']
    assert ShortenedURL.objects.count() == 1

@pytest.mark.django_db
def test_shortenedurl_serializer_create_invalid_data():
    """Test that the ShortenedURLSerializer can create a new shortened URL with invalid data."""
    data = {
       "original_url": "www.badurl.com",
    }
    serializer = ShortenedURLSerializer(data=data)
    assert not serializer.is_valid()
    assert 'original_url' in serializer.errors

@pytest.mark.django_db
def test_shortenedurl_serializer_read_only_fields():
    """Test read-only fields in the ShortenedURLSerializer."""
    data = {
        "original_url": "https://www.example.com",
    }
    inst = ShortenedURL.objects.create(original_url="https://www.example.com")

    update_data = {
        "original_url": "https://www.newexample.com",
        'short_code': 'abc123abc1',
        'created_at': '2023-10-01',
    }
    
    serializer = ShortenedURLSerializer(instance=inst, data=update_data)
    assert serializer.is_valid()
    updated_inst = serializer.save()
    assert updated_inst.original_url == update_data['original_url']
    assert updated_inst.short_code != update_data['short_code']
    assert updated_inst.created_at != update_data['created_at']
    