
import json

# from django.contrib.auth.models import User
from django.urls import reverse, path, include
# from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import Client

import pytest
from django_mock_queries.query import MockSet

from mock import Mock, sentinel
from rest_framework.exceptions import ValidationError


from imager.models import Photo
from imager_rest.viewsets import PhotoUploadView 
from imager_rest.serializers import PhotoSerializer


class TestPhotoManager:

    def test_upload_creation(self, mocker):
        expected_results = [
            
            Photo(
                pk = "10",
                file = 'http://0.0.0.0:8000/media/images/photo-1.jpeg',
                
                ),
        ]
        # django-mock-queries nos permite crear Mock QuerySets
        # para omitir el acceso a BD
        qs = MockSet(expected_results[0])

        mocker.patch.object(Photo.objects, 'get_queryset', return_value=qs)
        result = list(Photo.objects.all())

        assert result == expected_results
        assert str(result[0]) == str('Photo object (10)')


# Gives me error
# class TestViewSet:

#     @pytest.mark.urls('imager.urls')
#     def test_photos(self, rf, mocker):

#         url = reverse('photos')
#         request = rf.get(url)

#         queryset = MockSet(
#             Photo( pk='1', file='img1.jpg'),
#             Photo( pk='2', file='img2.jpg'),
#         )

#         mocker.patch.object(PhotoUploadView, 'get_queryset', return_value=queryset)
#         response = PhotoUploadView.as_view({'get': 'list'})(request).render()

#         assert response.status_code == 200
#         assert len(json.loads(response.content)) == 2


class TestPhotoSerializer:

    def test_expected_serialized_json(self):

        expected_results = {
            'pk': 1,
            'file': 'photo-1.jpeg',
        }

        photo = Photo(**expected_results)
        print('expected: ', expected_results)

        results = PhotoSerializer(photo).data
        
        #When 
        xp = {'pk': 1, 'file': '/media/photo-1.jpeg'}

        assert results == xp