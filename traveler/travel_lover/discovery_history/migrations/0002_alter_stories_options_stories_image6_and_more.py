# Generated by Django 4.2.2 on 2023-07-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discovery_history', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stories',
            options={'ordering': ['-created'], 'verbose_name': 'географическое открытие', 'verbose_name_plural': 'Географические открытия'},
        ),
        migrations.AddField(
            model_name='stories',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='stories/images/', verbose_name='Картинка6'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image',
            field=models.ImageField(upload_to='stories/images/', verbose_name='Картинка1'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='stories/images/', verbose_name='Картинка2'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='stories/images/', verbose_name='Картинка3'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='stories/images/', verbose_name='Картинка4'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='stories/images/', verbose_name='Картинка5'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
