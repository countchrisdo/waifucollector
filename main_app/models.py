from django.db import models
from django.urls import reverse

MEDIUMS = (
    ("G", "Video Game"),
    ("B", "Book"),
    ("A", "Anime")
)

# Create your models here.
class Waifu(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"waifu_id": self.id})

# A specific cameo a waifu has in a specific piece of media with a description of their role
class Cameo(models.Model):
    title = models.CharField(max_length=100)
    medium = models.CharField(
        max_length=1,
        choices=MEDIUMS,
        default="A"
        )
    description = models.TextField('Describe their Cameo here')

    waifu = models.ForeignKey(Waifu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} a {self.get_medium_display()}"
    
    class Meta:
        ordering = ["title"]