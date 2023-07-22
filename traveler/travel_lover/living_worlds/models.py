from django.db import models


class Worlds(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Статья')
    image = models.ImageField(upload_to='travels/images/', verbose_name='Картинка1')
    image2 = models.ImageField(upload_to='travels/images/', null=True, blank=True, verbose_name='Картинка2')
    image3 = models.ImageField(upload_to='travels/images/', null=True, blank=True, verbose_name='Картинка3')
    image4 = models.ImageField(upload_to='travels/images/', null=True, blank=True, verbose_name='Картинка4')
    image5 = models.ImageField(upload_to='travels/images/', null=True, blank=True, verbose_name='Картинка5')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'живой мир'
        verbose_name_plural = 'Живые миры'
        ordering = ['-created']

