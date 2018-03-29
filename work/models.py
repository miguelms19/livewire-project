from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Jobdetails(models.Model):
    image = models.ImageField(upload_to='images/', default='SOME STRING')
    jobtitle = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=2000)
    webaddress = models.CharField(max_length=2000, validators=[URLValidator()], blank=True)

    def __str__(self):
        return self.jobtitle[:100]
