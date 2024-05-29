from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Note(models.Model):
    URGENCY_CHOICES = (
        ('High', 'High'),
        ('Low', 'Low'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='3')

    def get_absolute_url(self):
        return reverse('aplikacjaNotatki:note_detail', args=[self.id])

    class Meta:
        ordering = ('urgency', 'created',)

    def __str__(self):
        return self.title
