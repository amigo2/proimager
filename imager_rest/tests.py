
# import json

# # from django.contrib.auth.models import User
# from django.urls import reverse, path, include
# # from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.test import Client

# import pytest
# from django_mock_queries.query import MockSet
# from rest_framework.exceptions import ValidationError


# from imager.models import Photo


# class TestPhotoManager:

#     def test_photo_creation(self, mocker):
#         expected_results = [
            
#             Photo(file ='img1.jpg'),
#         ]
#         # django-mock-queries nos permite crear Mock QuerySets
#         # para omitir el acceso a BD
#         qs = MockSet(expected_results[0])

#         mocker.patch.object(Photo.objects, 'get_queryset', return_value=qs)
#         result = list(Car.objects.get_cars_by_created(date))

#         assert result == expected_results
#         assert str(result[0]) == expected_results[0].code

# class PhotosAPITest(APITestCase):
    
#     def test_urls(self):
#         c = Client()
#         response = c.post('/login/', {'username': 'fer', 'password': '1818'})
#         response.status_code
#         response = c.get('photos/photos/p')
#         response.status_code



#         path('proimage.com/photos/', include('imager_rest.urls'))
        #base_url = reverse('imager_rest')