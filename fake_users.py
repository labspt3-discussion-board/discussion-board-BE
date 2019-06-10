import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

from api.models import User, Subtopic, Discussion, Comments
from faker import Faker

fake = Faker()


def create_non_premium_users(N):
    for _ in range(N):
        newuser = User.objects.get_or_create(
            uuid = fake.uuid4,
            username = fake.user_name,
            email = fake.email,
            password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        )


def create_premium_users(N):
    for _ in range(N):
        newuser = User.objects.get_or_create(
            uuid = fake.uuid4,
            username = fake.user_name,
            email = fake.email,
            password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
            premium = True
        )


create_non_premium_users(250)
create_premium_users(125)
print("Users created...")
