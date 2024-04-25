from django.core.management import BaseCommand
from shopapp.models import Product
from random import randint


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **kwargs):
        num = randint(1, 1000)
        new_product = Product(name_product=f'product{num}', description_product=f'description_product{num}',
                              price_product={num + 10}, quantity_product={num + 20}, added_date_product='2024-04-25')
        new_product.save()
        self.stdout.write(f'{new_product} creation')
