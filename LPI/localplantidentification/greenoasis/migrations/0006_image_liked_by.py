# Generated by Django 5.1 on 2024-11-02 08:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenoasis', '0005_image_like_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
