from django.db import models


class Stories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='stories/images/')
    image2 = models.ImageField(upload_to='stories/images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='stories/images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='stories/images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='stories/images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
