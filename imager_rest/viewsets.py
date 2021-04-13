from rest_framework import viewsets, generics
from django.contrib.auth.models import User, Group
from imager_rest.serializers import UploadImageSerializer, FileSerializer, PhotoSerializer
from imager.models import UploadImage, Photo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer


class FileUploadViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Photo.objects.all()


class PhotoUploadView(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()



            