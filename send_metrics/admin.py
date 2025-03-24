from django.contrib import admin
from solo.admin import SingletonModelAdmin

from send_metrics.models import MonitoringConfig


admin.site.register(MonitoringConfig, SingletonModelAdmin)
