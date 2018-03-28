from django.db import models
from django.core.validators import URLValidator
import PIL
from PIL import Image

# Create your models here.
class Team(models.Model):
    image = models.Image(upload_to='media/')
    name = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=2000)
    web = models.CharField(max_length=2000, validators=[URLValidator()], blank=True)

    def __str__(self):
        return self.name[:100]
