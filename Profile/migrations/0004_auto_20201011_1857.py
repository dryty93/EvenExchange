# Generated by Django 2.0.2 on 2020-10-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='Cloud 9', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
