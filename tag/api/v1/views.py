# from django_filters import rest_framework as filters
from tag.models import Tag
from .serializers import TagSerializer
from rest_framework import generics



# # Create your views here.
# class TagFilter(filters.FilterSet):
#     class Meta:
#         model = Tag
#         fields = {
#             'name': ['exact', 'icontains'],
#         }

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = TagFilter


class TagPost(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = TagFilter



class TagDetail(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDelete(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagUpdate(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
