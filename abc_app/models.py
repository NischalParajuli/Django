from django.db import models

# Create your models here.

class Todolist(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  status = models.BooleanField()
  end_by = models.DateTimeField()

