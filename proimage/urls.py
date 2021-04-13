
from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from imager import views
from imager_rest.viewsets import FileUploadViewSet
from imager_rest.viewsets import PhotoUploadView



router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('file', FileUploadViewSet, 'file')
router.register('photos', PhotoUploadView, 'photos')



# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('proimage.com/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),

    path('proimage.com/', include(router.urls)),
    path('proimage.com/', include('rest_framework.urls', namespace='rest_framework')),
    path("proimage.com/api/", include("imager_rest.urls")),
    path('upload/', include(router.urls)),
    path('photos/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)