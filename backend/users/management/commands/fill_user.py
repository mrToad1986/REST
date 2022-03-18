from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_1 = User(
            user_name='user1',
            first_name='Иван',
            last_name='Иванов',
            birthday_year=1990,
            email='user1@gb.local')
        user_1.save()

# выполняется в консоли коммандой python manage.py fill_user
# данные добавляются в http://127.0.0.1:8000/api/authors/
