from rest_framework import serializers
from imager.models import UploadImage, Photo

# Unused upload single Image
class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'image')
    
# Multiple file serializer
class FileSerializer(serializers.Serializer):

    # Nested list of list and file field to access 
    # the multiple files uploaded
    file = serializers.ListField(
                child=serializers.FileField( max_length=100000,
                                         allow_empty_file=False,
                                        use_url=False )
                                )

    # Creates a single photo file from the multiple files updated
    def create(self, validated_data):
        image=validated_data.pop('file')
        for img in image:
            photo=Photo.objects.create(file=img)
        return photo

    # Here it should go all the updates like the rotation and
    # other Filters
    # This should be extended to its own aaplication
    # def update(self, instance, validated_data):
    #     pass

    # Likewise delete whould be in another app
    # def delete(self, validated_data):
    #     pass

    
    # This is a trick to close thereutrn porperly as without this
    # was returning a weird error
    def to_representation(self, instance):
        return {'result':{'id':instance.id}}


# Photo View Serializer 
class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('pk', 'file')



        
        

    




