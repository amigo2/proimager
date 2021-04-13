from django.db import models


def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(),extension)

# This an unused model I create at the begining
class UploadImage(models.Model):
    image = models.ImageField('Upload image', upload_to=scramble_uploaded_filename)


# Simple class to save all files to photos
class Photo(models.Model):
    file = models.ImageField( upload_to=user_directory_path, default='pots/default.jpg')

    # class Meta:
    #     verbose_name_plural = 'Photos'

    # def __str__(self):
    #     """Prints the name of the Photo"""
    #     return f'{self} photos'