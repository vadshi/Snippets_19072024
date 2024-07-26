from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'get all users'

    def handle(self, *args, **options):
        return 'users: ' + ', '.join(user.username for user in User.objects.all())
