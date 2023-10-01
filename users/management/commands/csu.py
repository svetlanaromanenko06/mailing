import os


from config.settings import BASE_DIR
from django.core.management import BaseCommand
from users.models import User




class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='svroman07@gmail.com',
            first_name='Admin',
            last_name='Svet',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('venera18')
        user.save()