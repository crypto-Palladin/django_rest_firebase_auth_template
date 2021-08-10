from django.core.management.base import BaseCommand
from core.models import CustomUser
from firebase_auth_project.settings import INITIAL_USER_PASSWORD, INITIAL_USER_EMAIL


class Command(BaseCommand):

    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            admin = CustomUser.objects.create_superuser(email=INITIAL_USER_EMAIL, password=INITIAL_USER_PASSWORD)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print(f"_________________________________________________ \n"
                  f"Initial ADMIN ACCOUNT email={INITIAL_USER_EMAIL}, password={INITIAL_USER_PASSWORD}. \n"
                  f"DO CHANGE THE PASSWORD AFTER FIRST LOGIN \n"
                  f"_________________________________________________ \n")
