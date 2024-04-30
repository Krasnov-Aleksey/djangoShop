from django.core.management import BaseCommand
from shopapp.models import Client
from random import randint


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **kwargs):
        num = randint(1, 1000)
        phone = randint(1, 10000000000)
        new_client = Client(name_client=f'Svet{num}', email=f'Svet{num}@m.ru',
                            number_phone=f'{phone}', address=f'City-{num}',
                            registration_date_client='2023-04-30')
        new_client.save()
        self.stdout.write(f'{new_client} creation')


