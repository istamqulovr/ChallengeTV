from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Challenge(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=15, null=True, blank=True,unique=True)
    description = models.TextField()
    days = models.IntegerField()
    #start_time = models.TimeField()
    #end_time = models.TimeField()

    def __str__(self):
        return self.name

