# Generated by Django 2.0.2 on 2020-10-11 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AOI', '0008_auto_20200427_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, default='', upload_to='vids'),
        ),
    ]
