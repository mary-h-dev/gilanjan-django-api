from rest_framework import generics, permissions, viewsets
from blog.models import Blog, CommentsBlog, Category, BlogLike
from .serializers import (
    BlogSerializer, BlogCreateUpdateSerializer,
    CommentsBlogSerializer, CommentsBlogCreateSerializer,
    CategorySerializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .permissions import IsAuthorOrReadOnly



# Blog Views
class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]



class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
   



class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied("شما اجازه ویرایش این بلاگ را ندارید.")
        serializer.save()

# Comments Views


class BlogCommentsCreateView(generics.CreateAPIView):
    queryset = CommentsBlog.objects.all()
    serializer_class = CommentsBlogCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class BlogCommentsListView(generics.ListAPIView):
    queryset = CommentsBlog.objects.all()
    serializer_class = CommentsBlogSerializer
    permission_classes = [permissions.AllowAny]



class BlogCommentsDetailView(generics.RetrieveAPIView):
    queryset = CommentsBlog.objects.all()
    serializer_class = CommentsBlogSerializer
    permission_classes = [permissions.AllowAny]



class BlogCommentsUpdateView(generics.UpdateAPIView):
    queryset = CommentsBlog.objects.all()
    serializer_class = CommentsBlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied("شما اجازه ویرایش این کامنت را ندارید.")
        serializer.save()




# Blog Like and Visit Views
class BlogVisitCountView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        blog.view_count += 1
        blog.save()
        return Response({'view_count': blog.view_count})



class BlogLikeCountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        user = request.user
        like, created = BlogLike.objects.get_or_create(blog=blog, user=user)
        if not created:
            like.liked = not like.liked
            like.save()
        else:
            like.liked = True
            like.save()
        like_count = BlogLike.objects.filter(blog=blog, liked=True).count()
        return Response({'like_count': like_count})




# Category ViewSet
class BlogCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
