from celery import shared_task
from django.core.management import call_command


@shared_task
def send_plugins_metric_task():
    call_command("send_plugins_metric")
