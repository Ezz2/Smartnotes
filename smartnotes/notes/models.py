from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(null=True, blank=True, verbose_name="Date&Time Created")
