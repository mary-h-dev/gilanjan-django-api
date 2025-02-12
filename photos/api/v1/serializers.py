from rest_framework import serializers
from photos.models import Gallery, Photo



class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'gallery', 'image', 'title', 'description')




class GallerySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'photos')

    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        gallery = Gallery.objects.create(**validated_data)
        for photo_data in photos_data:
            Photo.objects.create(gallery=gallery, **photo_data)
        return gallery

