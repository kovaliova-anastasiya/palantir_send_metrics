import requests
from django.core.management.base import BaseCommand
from cms.models import CMSPlugin
from send_metrics.models import MonitoringConfig


class Command(BaseCommand):
    help = "Sends plugins metric to Palantir"

    def handle(self, *args, **kwargs):
        config = MonitoringConfig.get_solo()
        fields = {
            'api_url': config.api_url,
            'name': config.name,
            'group': config.group
        }

        missing_fields = [field for field, value in fields.items() if not value]

        if missing_fields:
            self.stdout.write(
                self.style.ERROR(f"Missing fields in MonitoringConfig: {', '.join(missing_fields)}")
            )
            return

        count = CMSPlugin.objects.count()
        data = {
            "plugins_count": count,
            "url": config.site_url,
            "name": config.name,
            "group": config.group,
        }

        response = requests.post(config.api_url, json=data)
        self.stdout.write(f"{response.status_code} {response.text}")

        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS("Data is sent successfully"))
        else:
            self.stdout.write(self.style.ERROR(f"Error {response.status_code}: {response.text}"))
