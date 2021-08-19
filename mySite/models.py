from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name