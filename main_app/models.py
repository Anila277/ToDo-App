from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    PRIORITY = (
        ('N', 'Need It Done Now!'),
        ('W', 'Can Wait Few Days.'),
        ('L', 'Can Be Done Later.'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY, default=PRIORITY[0][0])
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
