from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_26 = User(
            user_name='user26',
            first_name='Петр',
            last_name='Петров',
            birthday_year=1992,
            email='user2@gb.local',
            password='1111',)
        user_26.save()

# выполняется в консоли коммандой python manage.py fill_user
# данные добавляются в http://127.0.0.1:8000/api/users/
