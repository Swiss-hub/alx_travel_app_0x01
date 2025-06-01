from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.exists():
            user = User.objects.create_user(username='host1', password='password123')
        else:
            user = User.objects.first()

        sample_listings = [
            {
                "title": "Cozy Apartment in City Center",
                "description": "A nice and cozy apartment close to all attractions.",
                "location": "Downtown",
                "price_per_night": 75.00,
            },
            {
                "title": "Beachside Bungalow",
                "description": "Enjoy the sea breeze in this beautiful bungalow.",
                "location": "Seaside",
                "price_per_night": 120.00,
            },
            {
                "title": "Mountain Cabin Retreat",
                "description": "A peaceful cabin in the mountains, perfect for relaxation.",
                "location": "Mountain View",
                "price_per_night": 90.00,
            },
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "location": data["location"],
                    "price_per_night": data["price_per_night"],
                    "host": user,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Listing already exists: {listing.title}'))

        self.stdout.write(self.style.NOTICE('Seeding completed.'))
        self.stdout.write(self.style.NOTICE('Run `python manage.py seed` to seed the database with sample data.'))