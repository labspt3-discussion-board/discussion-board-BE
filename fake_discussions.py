import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User, Subforum, Discussion, Comments
from faker import Faker

fake = Faker()

def create_discussions(N):
    for _ in range(N):
        newdiscussion = Discussion.objects.get_or_create(
            title = fake.sentence(nb_words=2, variable_nb_words=True, ext_word_list=None),
            description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
            upvote = random.randint(0, 10000),
            downvote = random.randint(0, 10000),
            owner = User.objects.get(pk=random.randint(1, 696)),
            subforum = Subforum.objects.get(pk=random.randint(1, 10))
        )

create_discussions(500)
print("Users created...")
