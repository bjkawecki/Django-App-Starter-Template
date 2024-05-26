import logging

from allauth.account.models import EmailAddress
from celery import shared_task
from celery.signals import worker_ready
from django.utils import timezone
from django_celery_beat.models import ClockedSchedule, CrontabSchedule, PeriodicTask

from dj_app.models.user import User
from dj_app.services.settings import deactivate_user, send_deactivation_confirmation_email

logger = logging.getLogger("django")


@shared_task()
def send_delete_user_confirmation_email_task(user_email, user_id):
    email_obj = EmailAddress.objects.get(email=user_email)
    if not email_obj.verified:
        print("Deactivating user...")
        send_deactivation_confirmation_email(user_email)
        deactivate_user(user_id)
        print("User deactivated.")


@worker_ready.connect
def at_start(sender, **kwargs):
    """Run tasks at startup"""
    schedule_1, _ = CrontabSchedule.objects.get_or_create(
        # minute="*/1"
        minute="1",
        hour="1",
        day_of_month="1",
    )
    schedule_2, _ = CrontabSchedule.objects.get_or_create(
        # minute="*/1"
        minute="2",
        hour="1",
        day_of_month="1",
    )
    PeriodicTask.objects.get_or_create(
        crontab=schedule_1,
        name="Remove past periodic tasks",
        task="dj_app.tasks.remove_past_periodic_tasks",
    )

    PeriodicTask.objects.get_or_create(
        crontab=schedule_2,
        name="Remove users with unverified email",
        task="dj_app.tasks.remove_users_with_unverified_email",
    )


@shared_task()
def remove_past_periodic_tasks():
    logger.info("Collecting past periodic tasks for removing...")
    past_periodic_tasks = PeriodicTask.objects.filter(
        one_off=True, clocked__clocked_time__lt=timezone.now()
    )
    if not past_periodic_tasks:
        logger.info("No past periodic tasks in database to remove.")
    else:
        logger.info("Removing past periodic tasks from database...")
        for task in past_periodic_tasks:
            task.delete()
        past_clocked_schedules = ClockedSchedule.objects.filter(
            clocked_time__lt=timezone.now()
        )
        if past_clocked_schedules:
            for schedule in past_clocked_schedules:
                schedule.delete()
        logger.info("Past periodic tasks and clocked schedules from database removed.")


@shared_task
def remove_users_with_unverified_email():
    logger.info("Collecting unveryfied, active users for removing...")
    unverified_emails = EmailAddress.objects.filter(verified=False)
    if not unverified_emails:
        logger.info("No unveryfied, active users found.")
    else:
        for email in unverified_emails:
            unverified_users = User.objects.filter(email=email, is_active=True)
            logger.info("Unveryfied, active users found.")
            for user in unverified_users:
                logger.info(f"User {user} removed.")
                user.delete()
            logger.info("Unveryfied, active users removed.")
