from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', default='a.jpg')
    description = models.TextField()

    def __str__(self):
        return self.title