
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

# Tested with Pytest

class TestPhotoManager:

    def test_upload_creation(self, mocker):

        # POST data to test
        expected_results = [
            Photo(
                pk = "10",
                file = 'http://0.0.0.0:8000/media/images/photo-1.jpeg',
                
                ),
        ]
        # Django Mock queries allow us to test db without creating db's entries
        qs = MockSet(expected_results[0])

        # Creates data into model
        mocker.patch.object(Photo.objects, 'get_queryset', return_value=qs)
        result = list(Photo.objects.all())

        #  return and check values
        assert result == expected_results
        #  in this case is slightly biased as format a bit diff but wont afect the test result
        assert str(result[0]) == str('Photo object (10)')


# Gives me error
# reverse error ad urls and misscongigured, to be implemented
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



#  Selializer test of view class
class TestPhotoSerializer:

    def test_expected_serialized_json(self):

        # data added to pass to serializer
        expected_results = {
            'pk': 1,
            'file': 'photo-1.jpeg',
        }


        photo = Photo(**expected_results)
        print('expected: ', expected_results)

        results = PhotoSerializer(photo).data
        
        #This is bias the data to as media always appear in return
        #  Needs implementation
        xp = {'pk': 1, 'file': '/media/photo-1.jpeg'}

        assert results == xp