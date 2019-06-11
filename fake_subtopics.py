import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User, Subtopic, Discussion, Comments

def create_subtopics():
    s = ['memes','news','pics','funny','gaming','worldnews','todayilearned','aww','politics','mildlyinteresting']
    for i in range(len(s)):
        Subtopic.objects.get_or_create(
            name = s[i],
            owner = User.objects.get(pk=random.randint(1, 620)))

create_subtopics()
print('Subtopics created...')
