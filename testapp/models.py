from django.db import models

class Discussion(models.Model):
    topic = models.CharField(max_length=30)
