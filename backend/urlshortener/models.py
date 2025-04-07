from django.db import models
from django.contrib.auth.models import User

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.short_code