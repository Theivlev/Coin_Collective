import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from gathering.models import Collect, Payment


class Command(BaseCommand):
    help = 'Заполнение бд тестовыми данными'

    def handle(self, *args, **options):
        for i in range(500):
            username = 'user' + str(i)
            password = 'password123'
            email = 'user' + str(i) + '@yandex.com'
            User.objects.create_user(
                username=username, password=password, email=email
                )

        for i in range(1000):
            author = random.choice(User.objects.all())
            collect = Collect.objects.create(
                author=author,
                gathering_name='Collect ' + str(i),
                donation_purpose='Purpose ' + str(i),
                description='Description ' + str(i),
                all_amount=random.randint(1000, 10000),
                end_datetime='2023-12-31 23:59:59'
            )

        for collect in Collect.objects.all():
            for i in range(random.randint(1, 5)):
                random_user = random.choice(User.objects.all())
                Payment.objects.create(
                    collect=collect,
                    amount=random.randint(10, 100),
                    donator=random_user
                    )
        self.stdout.write(
            self.style.SUCCESS('База данных заполнена тестовыми данными'))
