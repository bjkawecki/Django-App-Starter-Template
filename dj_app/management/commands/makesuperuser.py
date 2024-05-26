import logging

from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

logger = logging.getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        first_name = "John"
        last_name = "Doe"
        email = "admin@mail.org"
        new_password = "admin"
        try:
            u = None

            if User.objects.filter(is_superuser=True).exists():
                self.stdout.write("No superuser exists in the database.")
                self.stdout.write("Deleting superuser...")
                User.objects.filter(is_superuser=True).delete()

            self.stdout.write("Creating new superuser...")
            u = User.objects.create_superuser(  # noqa: F841
                email=email,
                password=new_password,
                first_name=first_name,
                last_name=last_name,
            )

            self.stdout.write(f"Vorname:{first_name}")
            self.stdout.write(f"Nachname:{last_name}")
            self.stdout.write(f"Email: {email}")
            self.stdout.write(f"Password: {new_password}")
            self.stdout.write("Done.")
            self.stdout.write("Creating new EmailAdress for superuser.")
            email, created = EmailAddress.objects.get_or_create(
                email=u.email, user=u, verified=True
            )
            if created:
                self.stdout.write("Done.")
            self.stdout.write("==========================")
        except Exception as e:
            logger.error(e)
            self.stdout.write(f"There was an errer: {e}")
