from django.db import models
from django.core.validators import URLValidator
from django.core.files.storage import FileSystemStorage
from s3direct.fields import S3DirectField


fs = FileSystemStorage(location='/media/images')
# Create your models here.
class Job(models.Model):
    #image = models.ImageField(storage=fs)
    image = S3DirectField(dest='media')
    title = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=2000)
    web = models.CharField(max_length=2000, validators=[URLValidator()], blank=True)

    def __str__(self):
        return self.title[:100]
