# Generated by Django 2.0.2 on 2020-10-12 01:49

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=40)),
                ('body', models.TextField(default='Enter your message here', max_length=1000)),
                ('time_sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(default='', on_delete=False, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(default='', on_delete=False, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]