# Generated by Django 2.0.2 on 2020-04-28 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AOI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('summary', models.TextField(blank=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(default='default.jpg', upload_to='aoi_pics')),
                ('author', models.ForeignKey(default='', on_delete=False, to=settings.AUTH_USER_MODEL)),
                ('fans', models.ManyToManyField(related_name='fans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1500)),
                ('text', models.TextField(blank=True)),
                ('video', models.FileField(blank=True, upload_to='')),
                ('image', models.ImageField(blank=True, upload_to='post_images')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('chi_gained', models.IntegerField(blank=True, default=0)),
                ('slug', models.SlugField(default='')),
                ('aoi', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='aoi_name', to='AOI.AOI')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AOI.Post'),
        ),
    ]
