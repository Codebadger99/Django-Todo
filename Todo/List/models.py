from django.db import models

# Create your models here.
class list(models.Model):
    title     = models.CharField(blank=True, max_length=50, unique=True)
    completed = models.BooleanField(default=False)
    