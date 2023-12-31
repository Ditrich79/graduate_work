# Generated by Django 4.2.2 on 2023-07-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='stories/images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='stories/images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='stories/images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='stories/images/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='stories/images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
