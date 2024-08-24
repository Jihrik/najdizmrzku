from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    postal = models.CharField(max_length=6)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)  # No default needed here

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name
    