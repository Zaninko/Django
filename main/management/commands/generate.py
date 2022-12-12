from random import randint
from django.core.management.base import BaseCommand, CommandError
from main.models import Book
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Create fake information'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Кількість експонатів для додавання')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            fake = Faker()
            try:
                 a = fake.name()
                 ttl = fake.sentences(1)[0]
                 txt = ' '.join(fake.sentences(3))
                 pub = fake.year()
                 c = random.randint(1, 20)
                 obj = Book.objects.create(
                    title=ttl,
                    author=a,
                    text=txt,
                    published=pub,
                    count=c
                 )
            except:
                raise CommandError('Error of creating')
            else:
                print(f'{i+1} експонатів додалось')
















