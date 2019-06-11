import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User, Subtopic, Discussion, Comments
from faker import Faker

fake = Faker()

def create_comments(N):
    for _ in range(N):
        newcomments = Comments.objects.get_or_create(
            text = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
            owner = User.objects.get(pk=random.randint(1, 620)),
            discussion_id = Discussion.objects.get(pk=random.randint(1, 1362))
        )

create_comments(1500)
print("Creating comments...")
