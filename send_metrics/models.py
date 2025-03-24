from solo.models import SingletonModel
from django.db import models


class MonitoringConfig(SingletonModel):
    api_url = models.TextField()
    site_url = models.URLField()
    name = models.CharField(max_length=100, null=True, blank=True)
    group = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.api_url
