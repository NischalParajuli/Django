from django.db import models


class Todolist(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    status = models.BooleanField(default=False)   # FIX: added default=False so new tasks start as incomplete
  

    def __str__(self):
        return self.title