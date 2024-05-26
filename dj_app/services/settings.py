import json
from datetime import datetime, timedelta

from django.core.mail import EmailMessage
from django_celery_beat.models import ClockedSchedule, PeriodicTask

from dj_app.models.user import User


def send_deactivate_account_email(user_email):
    body = (
        "Hallo!\n\n"
        "Ihr Konto wurde von Ihnen zur Löschung markiert und ist nun deaktiviert.\n"
        "Falls dies ein Versehen war, melden Sie sich bitte umgehend an, um Ihr Konto erneut zu aktivieren.\n"
        "Andernfalls wird Ihr Konto in Kürze gelöscht und Ihr Fortschritt geht unwiderruflich verloren.\n\n"
        "Ihr App-Team"
    )
    email = EmailMessage(
        subject="Ihr Konto wurde deaktiviert",
        body=body,
        from_email="{{ app_name }} <kontakt@{{ app_name }}.de>",
        to=[user_email],
    )
    email.send(fail_silently=True)


def send_delete_user_confirm_email(email_obj, user_id):
    user_email = email_obj.email
    datetime_now = datetime.now()
    send_date = datetime_now + timedelta(days=3)
    clocked, _ = ClockedSchedule.objects.get_or_create(clocked_time=send_date)
    PeriodicTask.objects.create(
        clocked=clocked,
        name=f"delete_user_confirmation_email_{user_email}_{datetime_now}",
        task="trainer.tasks.send_delete_user_confirmation_email_task",
        kwargs=json.dumps({"user_email": user_email, "user_id": user_id}),
        one_off=True,
    )


def deactivate_user(user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()


def send_deactivation_confirmation_email(user_email):
    body = (
        "Hallo!\n\n"
        "Ihr {{ app_name }}-Konto wurde gelöscht.\n"
        "Vielen Dank für die Nutzung von {{ app_name }}.\n\n"
        "Ihr {{ app_name }}-Team"
    )
    email = EmailMessage(
        subject="Ihr Konto wurde gelöscht",
        body=body,
        from_email="{{ app_name }} <kontakt@{{ app_name }}.de>",
        to=[user_email],
    )
    email.send(fail_silently=False)
