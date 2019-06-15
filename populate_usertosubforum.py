import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User, Subforum, UserToSubforum

def populate_table(N):
    for _ in range(N):
        r = random.randint(1, 696)
        print(r)
        row = UserToSubforum.objects.get_or_create(
            user = User.objects.get(pk=r),
            username = User.objects.get(pk=r),
            subtopic = Subforum.objects.get(pk=random.randint(1, 10))
        )

populate_table(250)
print("Table Populated...")
