# Generated by Django 3.2.6 on 2021-08-31 06:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friends',
            new_name='Friend',
        ),
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
