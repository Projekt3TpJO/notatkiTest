from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    URGENCY_CHOICES = {0: "Low", 1: "Medium", 2: "High"}
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    urgency = models.CharField(max_length=6, choices=URGENCY_CHOICES, default=0)

    def __str__(self):
        return self.title
