# Generated by Django 3.1.3 on 2020-11-30 07:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_review_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Revieww',
        ),
    ]
