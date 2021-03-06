from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_async_email(subject, message, email_from, user_email):
    send_mail(subject, message, email_from, [user_email])
