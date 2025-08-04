from django.contrib.admin.models import CHANGE
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Challenge(models.Model):
    CHANGE_STATUS = [
        ("active", "active"),
        ("done", "done"),
        ("inprogress", "IN PROGRESS"),
        ("canceled", "CANCELED"),
        ("delayed",  "DELAYED"),
    ]

    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=15, null=True, blank=True, unique=True)
    description = models.TextField()
    days = models.IntegerField()
    status = models.CharField(choices=CHANGE_STATUS, null=True, blank=True)

    def get_status_display_class(self):
        return f"status-{self.status}"


    def __str__(self):
        return self.name

