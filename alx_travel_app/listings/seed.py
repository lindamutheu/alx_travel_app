import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Create or get a host user
        host, created = User.objects.get_or_create(
            email='host@example.com',
            defaults={
                'first_name': 'Host',
                'last_name': 'User',
                'password': 'admin123',  # Will need to set password properly if authenticating
                'role': 'host'
            }
        )

        if created:
            host.set_password('admin123')  # securely hash password
            host.save()

        # Create sample listings
        for _ in range(10):
            listing = Listing.objects.create(
                property_id=uuid.uuid4(),
                host=host,
                name=fake.company(),
                description=fake.text(max_nb_chars=200),
                location=fake.city(),
                price_per_night=random.randint(50, 500),
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.name}"))
