from django.db import models
from django.db import models

class Message(models.Model):
    status = models.IntegerField()
    message = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
