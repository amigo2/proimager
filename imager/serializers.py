from django.contrib.auth.models import User, Group
from rest_framework import serializers




# User serializer just to see users
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# Unused bgroup serializer
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class FileSerializer(serializers.Serializer):
#     file = serializers.FileField(max_length=None, allow_empty_file=False)