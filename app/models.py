# -*- coding: utf-8 -*-
from django.db import models


class Book(models.Model):
    """
    Class that manages the Book model fields
    """
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30, blank=True)
    pages = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.title
