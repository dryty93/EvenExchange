# Generated by Django 2.0.2 on 2020-04-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AOI', '0005_auto_20200427_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aoi',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='aoi_pics'),
        ),
    ]
