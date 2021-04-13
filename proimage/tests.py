import json
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.test import Client

client = APIClient()


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('registration/', include('rest_auth.registration.urls')),
        path('proimage.com/login/', include('rest_auth.urls')),

    ]

    #Test case create a new user
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        self.client = Client()
        self.user = User(username="testuser", email="testemail@test.com")
        self.user.is_staff = True
        self.user.set_password('secret')
        self.user.save()


    def test_login(self):
        """
        Ensure user can login.
        """
        user = User.objects.create_user(username='test1', password='testpass')
        self.client.login(username=user.username, password='testpass')


        


# class PhotosAPITest(APITestCase):
#     base_url = reverse('photos')




# import json

# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
# from rest_framework import status
# from imager_rest.viewsets import PhotoUploadView


# from . import urls

# from rest_framework.test import APIRequestFactory


# from rest_framework.test import APIClient

# client = APIClient()
# client.get('/photos/', {'photos': ''}, format='json')

# PHOTOS_URL = reverse('photos')

# class PhotosTest(APITestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User(username="testuser", email="testemail@test.com")
#         self.user.is_staff = True
#         self.user.set_password('secret')
#         self.user.save()

# factory = APIRequestFactory()
# #user = User.objects.get(username='fer')
# view = PhotoUploadView.as_view({'get': 'list'})

# # Make an authenticated request to the view...
# request = factory.get('/photos/photos/')
# #force_authenticate(request, user=user)
# response = view(request)


# class RegistrationTestCase(APITestCase):

    

    # def test_registration(self):
    #     data = {"username": "testcase", "email": "amigo@gmail.com"  ,"password1":"12345678P","password2":"12345678P"  }
    #     response = self.client.post("registration/", data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_login(self):
    #     data = {"username": "fer","password":"1818"  }
    #     response = self.client.post("proimage/login/", data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)