from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import GallerySerializer , PhotoSerializer
from rest_framework import generics, permissions
from photos.models import Gallery, Photo
from .permissions import IsAdminOrReadOnly



class GalleryUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        photos_data = []
        images = request.FILES.getlist('images')
        titles = request.data.getlist('titles', [])
        descriptions = request.data.getlist('descriptions', [])

        for idx, image in enumerate(images):
            photo_data = {'image': image}
            if idx < len(titles):
                photo_data['title'] = titles[idx]
            if idx < len(descriptions):
                photo_data['description'] = descriptions[idx]
            photos_data.append(photo_data)

        data['photos'] = photos_data

        serializer = GallerySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]



class GalleryDetailView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]



class PhotoListView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.AllowAny]



class PhotoDetailView(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.AllowAny]
