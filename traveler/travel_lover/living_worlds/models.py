from django.db import models


class Worlds(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='travels/images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
