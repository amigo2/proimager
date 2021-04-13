import json
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.test import Client

client = APIClient()


# Tested with unittest rest

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


