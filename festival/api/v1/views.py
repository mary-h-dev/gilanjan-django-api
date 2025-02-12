from rest_framework import generics, permissions
from festival.models import Festival
from .serializers import FestivalSerializer
from .permissions import IsAdminOrReadOnly

class FestivalCreateView(generics.CreateAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [permissions.IsAdminUser]

class FestivalListView(generics.ListAPIView):
    queryset = Festival.objects.filter(is_active=True)
    serializer_class = FestivalSerializer
    permission_classes = [permissions.AllowAny]

class FestivalDetailView(generics.RetrieveAPIView):
    queryset = Festival.objects.filter(is_active=True)
    serializer_class = FestivalSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

class FestivalUpdateView(generics.UpdateAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'slug'

class FestivalDeleteView(generics.DestroyAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'slug'
