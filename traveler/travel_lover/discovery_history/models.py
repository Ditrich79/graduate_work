from django.db import models


class Stories(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Статья')
    image = models.ImageField(upload_to='stories/images/', verbose_name='Картинка1')
    image2 = models.ImageField(upload_to='stories/images/', null=True, blank=True, verbose_name='Картинка2')
    image3 = models.ImageField(upload_to='stories/images/', null=True, blank=True, verbose_name='Картинка3')
    image4 = models.ImageField(upload_to='stories/images/', null=True, blank=True, verbose_name='Картинка4')
    image5 = models.ImageField(upload_to='stories/images/', null=True, blank=True, verbose_name='Картинка5')
    image6 = models.ImageField(upload_to='stories/images/', null=True, blank=True, verbose_name='Картинка6')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'географическое открытие'
        verbose_name_plural = 'Географические открытия'
        ordering = ['-created']
