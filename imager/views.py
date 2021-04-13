from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from imager.serializers import UserSerializer, GroupSerializer


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @api_view(["GET"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])  
# def welcome(request):
#     content = {"message": "Welcome to the BookStore!"}
#     return JsonResponse(content)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]



# class FileUploadViewSet(viewsets.ViewSet):

#     queryset = User.objects.none() 

#     def create(self, request):
#         serializer_class = FileSerializer(data=request.data)
#         if 'file' not in request.FILES or not serializer_class.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             #Multiple Files
#             files = request.FILES.getlist('file')
#             for f in files:
#                 handle_uploaded_file(f)
#             return Response(status=status.HTTP_201_CREATED)


# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

