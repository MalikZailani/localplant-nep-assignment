# Generated by Django 5.1 on 2024-10-20 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.SlugField(unique=True)),
                ('tags', models.TextField()),
                ('image', models.FileField(upload_to='pic/%y/')),
            ],
        ),
    ]
