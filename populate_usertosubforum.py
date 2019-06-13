import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User, Subforum, UserToSubforum

def populate_table(N):
    for _ in range(N):
        row = UserToSubforum.objects.get_or_create(
            user = User.objects.get(pk=random.randint(1, 564)),
            subtopic = Subforum.objects.get(pk=random.randint(15, 24))
        )

populate_table(250)
print("Table Populated...")
