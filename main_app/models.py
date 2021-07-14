from django.db import models
from django.urls import reverse

# Create your models here.
class Waifu(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"waifu_id": self.id})

