# Generated by Django 3.2 on 2021-04-12 05:58

from django.db import migrations, models
import imager.models


class Migration(migrations.Migration):

    dependencies = [
        ('imager', '0005_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='pots/default.jpg', upload_to=imager.models.user_directory_path),
        ),
    ]