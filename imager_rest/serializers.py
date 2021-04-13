from rest_framework import serializers
from imager.models import UploadImage, Photo

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'image')
    
    
class FileSerializer(serializers.Serializer):
    file = serializers.ListField(
                child=serializers.FileField( max_length=100000,
                                         allow_empty_file=False,
                                        use_url=False )
                                )

    
    def create(self, validated_data):
        image=validated_data.pop('file')
        for img in image:
            photo=Photo.objects.create(file=img)
        return photo


    # def update(self, instance, validated_data):
    #     pass

    # def delete(self, validated_data):
    #     pass

    

    def to_representation(self, instance):
        return {'result':{'id':instance.id}}



class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('pk', 'file')



        
        

    




