# Generated by Django 4.2.2 on 2023-07-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('living_worlds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worlds',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='travels/images/'),
        ),
        migrations.AddField(
            model_name='worlds',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='travels/images/'),
        ),
        migrations.AddField(
            model_name='worlds',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='travels/images/'),
        ),
        migrations.AddField(
            model_name='worlds',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='travels/images/'),
        ),
    ]
