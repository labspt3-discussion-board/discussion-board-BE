import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User, Subtopic, Discussion, Comments
from faker import Faker

fake = Faker()

def create_discussions(N):
    for _ in range(N):
        newdiscussion = Discussion.objects.get_or_create(
            title = fake.sentence(nb_words=2, variable_nb_words=True, ext_word_list=None),
            description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
            upvote = random.randint(0, 999),
            downvote = random.randint(0, 999),
            owner = User.objects.get(pk=random.randint(1, 620)),
            subtopic = Subtopic.objects.get(pk=random.randint(1, 10))
        )

create_discussions(500)
print("Users created...")
