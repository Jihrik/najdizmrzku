from django.db import models
from django.contrib.auth.models import User

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
    
    
class Rating(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Rating {self.rating} by {self.user.username}'