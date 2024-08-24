from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    postal = models.CharField(max_length=6) # using Charfield to ensure no digits will be lost vith save() method
