from django.db import models


class Travels(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='travels/images/')
    image2 = models.ImageField(upload_to='travels/images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='travels/images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='travels/images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='travels/images/', null=True, blank=True)

    def __str__(self):
        return self.title
