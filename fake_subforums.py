import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussionboard.settings')

import django
django.setup()

import random

from api.models import User, Subforum, Discussion, Comments

def create_subforums():
    s = ['memes','news','pics','funny','gaming','worldnews','todayilearned','aww','politics','mildlyinteresting']
    for i in range(len(s)):
        Subforum.objects.get_or_create(
            name = s[i],
            owner = User.objects.get(pk=random.randint(1, 10)))

create_subforums()
print('Subforums created...')
