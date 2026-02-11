from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = 'Seed sample products'

    def handle(self, *args, **options):
        sample = [
            {'name': 'Red T-Shirt', 'description': 'Comfortable red t-shirt', 'price': '19.99'},
            {'name': 'Blue Jeans', 'description': 'Stylish blue jeans', 'price': '49.99'},
            {'name': 'Sneakers', 'description': 'Running sneakers', 'price': '79.99'},
            {'name': 'Coffee Mug', 'description': 'Ceramic mug for coffee', 'price': '9.99'},
            {'name': 'Wireless Mouse', 'description': 'Ergonomic wireless mouse', 'price': '24.99'},
        ]
        Product.objects.all().delete()
        for p in sample:
            Product.objects.create(name=p['name'], description=p['description'], price=p['price'])
        self.stdout.write(self.style.SUCCESS('Seeded products'))
