from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from rest_framework import routers
from imager import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    #url(r'^api/', include('imager_rest.urls', namespace='api')),
    #url(r'^', include(router.urls)),
]
