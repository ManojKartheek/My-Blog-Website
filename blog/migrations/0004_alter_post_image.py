# Generated by Django 5.1.4 on 2024-12-09 06:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name="posts_img's"),
        ),
    ]
