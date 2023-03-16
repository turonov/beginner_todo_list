from django.db import models
class TODOlist(models.Model):
    task = models.CharField(max_length=20),
    description = models.TextField(),
    completed = models.BooleanField(default=False),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.