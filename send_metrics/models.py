import uuid
from django.db import models
from solo.models import SingletonModel


class MonitoringConfig(SingletonModel):
    api_url = models.TextField()
    site_url = models.URLField()
    name = models.CharField(max_length=100, null=True, blank=True)
    group = models.CharField(max_length=100, null=True, blank=True)
    api_key = models.CharField(
        help_text="Leave empty — it will be generated automatically upon saving",
        max_length=128,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return self.api_url
