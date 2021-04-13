# Generated by Django 3.2 on 2021-04-11 11:56

from django.db import migrations, models
import imager.models


class Migration(migrations.Migration):

    dependencies = [
        ('imager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to=imager.models.scramble_uploaded_filename, verbose_name='Upload image'),
        ),
    ]