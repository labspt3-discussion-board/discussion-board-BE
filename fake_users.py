import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User
from faker import Faker

fake = Faker()

def create_users(N):
    for _ in range(N):
        newuser = User.objects.get_or_create(
        uuid = fake.uuid4,
        username = fake.user_name,
        email = fake.email,
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))

create_users(400)
print("Users created...")
