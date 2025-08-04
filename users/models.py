
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

from challenge.models import Challenge
from .forms import RegisterForm

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ("other", "Другое")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    challenges = models.ManyToManyField(Challenge, blank=True)


    def __str__(self):
        return f"{self.user.username} профиль"




class UserChallenges(models.Model):
    users = models.ForeignKey(UserProfile, on_delete=CASCADE, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=CASCADE, null=True, blank=True)
    start_time = models.TimeField(auto_created=True)
    end_time = models.TimeField(auto_now=True)
