from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username='demo-user').exists():
            User.objects.create_user(username= 'demo-user',
                                    email='demo-user@super.com',
                                    password='1234',
                                    is_staff=True,
                                    is_active=True,
                                    is_superuser=True
            )
