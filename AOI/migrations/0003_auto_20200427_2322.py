# Generated by Django 2.0.2 on 2020-04-28 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AOI', '0002_auto_20200427_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aoi',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='aoi_pics'),
        ),
    ]