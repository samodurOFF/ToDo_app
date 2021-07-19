from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from users.models import User


class Command(BaseCommand):
    help = '''
    Creates some random users. 
    Insert number of users you want to create after the name of script like this:
    python manage.py create_users <number_of_users>
    '''

    def add_arguments(self, parser):
        parser.add_argument('numbers', type=int, help='number of users')

    def handle(self, *args, **kwargs):
        number_of_users = kwargs['numbers']
        for i in range(number_of_users):
            username, first_name, last_name = (get_random_string(length=10) for i in range(3))
            email = f'{username}@mail.com'
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password='password',
            )
