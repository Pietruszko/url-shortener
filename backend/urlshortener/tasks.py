from celery import shared_task
from django.db.models import F
from .models import ShortenedURL

@shared_task(bind=True, max_retries=3)
def track_click(self, short_code):
    """Async task to track a click on a shortened URL."""
    try:
        ShortenedURL.objects.filter(short_code=short_code).update(
            clicks=F('clicks') + 1
        )
    except Exception as e:
        self.retry(exc=e, countdown=60)