from django.core.management.base import BaseCommand
from library.models import Author

class Command(BaseCommand):
    def handle(self, *args, **options):
        author1 = Author(
            first_name='Иван',
            last_name='Бунин',
            birthday_year=1870,
            email='iab@google.com'
        )
        author1.save()

# выполняется в консоли коммандой python manage.py fill_user
# данные в http://127.0.0.1:8000/api/authors/ добавляются
# очень криво, надо переписать