from django.db import models
from uuid import uuid1

class Book(models.Model):
    title = models.CharField(max_length=200, null= False, blank=False)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

