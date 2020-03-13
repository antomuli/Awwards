from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100,blank=true)

    def __str__(self):
        return self.description