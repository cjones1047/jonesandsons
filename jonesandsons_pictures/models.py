from django.db import models

# Create your models here.
class Pictures(models.Model):
    PictureId = models.AutoField(primary_key=True)
    PictureFileName = models.CharField(max_length=100)
