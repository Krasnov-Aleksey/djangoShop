from django.core.management import BaseCommand
from shopapp.models import Order
from random import randint
from decimal import Decimal


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **kwargs):
        num = randint(1, 1000)
        num2 = Decimal(f'{num}.15')
        num3 = Decimal(f'{num}.002')
        new_product = Product(name_product=f'product{num}', description_product=f'description_product{num}',
                              price_product=f'{num2}', quantity_product=f'{num3}',
                              added_date_product='2024-04-25')
        new_product.save()
        self.stdout.write(f'{new_product} creation')
